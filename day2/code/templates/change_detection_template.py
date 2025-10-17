"""
Change Detection Template for Google Earth Engine
Detect land cover changes using classified images

Usage: Copy and adapt for Session 2 NRM applications
"""

import ee
import pandas as pd

def detect_forest_loss(classification_t1, classification_t2, forest_classes=[1, 2]):
    """
    Detect forest loss between two time periods
    
    Parameters:
    -----------
    classification_t1 : ee.Image
        Earlier classification (e.g., 2020)
    classification_t2 : ee.Image
        Later classification (e.g., 2024)
    forest_classes : list
        Class IDs representing forest (default: [1, 2] for primary/secondary)
    
    Returns:
    --------
    ee.Image : Forest loss map (1 = loss, 0 = no change)
    """
    
    # Create forest masks
    forest_t1 = classification_t1.eq(forest_classes[0])
    for class_id in forest_classes[1:]:
        forest_t1 = forest_t1.Or(classification_t1.eq(class_id))
    
    forest_t2 = classification_t2.eq(forest_classes[0])
    for class_id in forest_classes[1:]:
        forest_t2 = forest_t2.Or(classification_t2.eq(class_id))
    
    # Detect loss: forest in t1, not forest in t2
    forest_loss = forest_t1.And(forest_t2.Not()).rename('forest_loss')
    
    return forest_loss


def create_change_matrix(classification_t1, classification_t2):
    """
    Create from-to change matrix
    
    Returns:
    --------
    ee.Image : Change code (from_class * 10 + to_class)
    
    Example: Forest (1) to Agriculture (4) = 14
    """
    
    # Multiply t1 by 10 and add t2
    change_code = classification_t1.multiply(10).add(classification_t2).rename('change_code')
    
    return change_code


def calculate_class_transitions(change_matrix, from_class, to_classes, aoi, scale=10):
    """
    Calculate area of transitions from one class to others
    
    Parameters:
    -----------
    change_matrix : ee.Image
        Change code image (from create_change_matrix)
    from_class : int
        Source class ID
    to_classes : list
        Destination class IDs
    aoi : ee.Geometry
        Area of interest
    scale : int
        Pixel size in meters
    
    Returns:
    --------
    dict : Area in hectares for each transition
    """
    
    transitions = {}
    
    for to_class in to_classes:
        # Calculate change code
        change_code = from_class * 10 + to_class
        
        # Create mask for this transition
        transition_mask = change_matrix.eq(change_code)
        
        # Calculate area
        area = transition_mask.multiply(ee.Image.pixelArea()).reduceRegion(
            reducer=ee.Reducer.sum(),
            geometry=aoi,
            scale=scale,
            maxPixels=1e13
        )
        
        # Convert to hectares
        area_ha = ee.Number(area.get('change_code')).divide(10000)
        
        transitions[f'{from_class}_to_{to_class}'] = area_ha.getInfo()
    
    return transitions


def detect_deforestation_hotspots(forest_loss, aoi, kernel_radius=500):
    """
    Identify deforestation hotspots using focal statistics
    
    Parameters:
    -----------
    forest_loss : ee.Image
        Binary forest loss image
    aoi : ee.Geometry
        Area of interest
    kernel_radius : int
        Radius in meters for hotspot detection
    
    Returns:
    --------
    ee.Image : Hotspot intensity (0-1)
    """
    
    # Create circular kernel
    kernel = ee.Kernel.circle(radius=kernel_radius, units='meters')
    
    # Calculate focal mean (proportion of loss pixels nearby)
    hotspots = forest_loss.focalMean(kernel=kernel, iterations=1).rename('hotspot_intensity')
    
    return hotspots.clip(aoi)


def analyze_agricultural_expansion(change_matrix, forest_classes=[1, 2], ag_class=4, aoi=None):
    """
    Analyze forest to agriculture conversion
    
    Returns:
    --------
    dict : Statistics on agricultural expansion
    """
    
    results = {}
    
    for forest_class in forest_classes:
        # Forest to agriculture change code
        change_code = forest_class * 10 + ag_class
        
        # Create mask
        conversion_mask = change_matrix.eq(change_code)
        
        # Calculate area
        if aoi:
            area = conversion_mask.multiply(ee.Image.pixelArea()).reduceRegion(
                reducer=ee.Reducer.sum(),
                geometry=aoi,
                scale=10,
                maxPixels=1e13
            )
            area_ha = ee.Number(area.get('change_code')).divide(10000).getInfo()
        else:
            area_ha = 0
        
        class_name = 'Primary Forest' if forest_class == 1 else 'Secondary Forest'
        results[f'{class_name}_to_Agriculture_ha'] = area_ha
    
    results['Total_Forest_to_Ag_ha'] = sum(results.values())
    
    return results


def create_change_report(classification_t1, classification_t2, aoi, year1, year2, class_names):
    """
    Generate comprehensive change detection report
    
    Parameters:
    -----------
    classification_t1 : ee.Image
        Earlier classification
    classification_t2 : ee.Image
        Later classification
    aoi : ee.Geometry
        Area of interest
    year1, year2 : int
        Years of classifications
    class_names : dict
        Mapping of class IDs to names (e.g., {1: 'Primary Forest', 2: 'Secondary Forest', ...})
    
    Returns:
    --------
    dict : Comprehensive change statistics
    """
    
    report = {
        'period': f'{year1}-{year2}',
        'area_changes': {},
        'key_transitions': {},
        'summary': {}
    }
    
    # Calculate area for each class in both periods
    def calculate_class_area(classification, class_id):
        mask = classification.eq(class_id)
        area = mask.multiply(ee.Image.pixelArea()).reduceRegion(
            reducer=ee.Reducer.sum(),
            geometry=aoi,
            scale=10,
            maxPixels=1e13
        )
        return ee.Number(area.get('classification')).divide(10000).getInfo()
    
    # Area changes for each class
    for class_id, class_name in class_names.items():
        area_t1 = calculate_class_area(classification_t1, class_id)
        area_t2 = calculate_class_area(classification_t2, class_id)
        change = area_t2 - area_t1
        percent_change = (change / area_t1 * 100) if area_t1 > 0 else 0
        
        report['area_changes'][class_name] = {
            f'{year1}_ha': round(area_t1, 2),
            f'{year2}_ha': round(area_t2, 2),
            'change_ha': round(change, 2),
            'percent_change': round(percent_change, 2)
        }
    
    # Key transitions (simplified)
    change_matrix = create_change_matrix(classification_t1, classification_t2)
    
    # Forest loss
    forest_loss_img = detect_forest_loss(classification_t1, classification_t2, [1, 2])
    forest_loss_area = forest_loss_img.multiply(ee.Image.pixelArea()).reduceRegion(
        reducer=ee.Reducer.sum(),
        geometry=aoi,
        scale=10,
        maxPixels=1e13
    ).get('forest_loss')
    report['key_transitions']['forest_loss_ha'] = ee.Number(forest_loss_area).divide(10000).getInfo()
    
    # Agricultural expansion
    ag_expansion = analyze_agricultural_expansion(change_matrix, [1, 2], 4, aoi)
    report['key_transitions']['agricultural_expansion'] = ag_expansion
    
    # Summary statistics
    total_area = aoi.area().divide(10000).getInfo()
    report['summary'] = {
        'total_study_area_ha': round(total_area, 2),
        'forest_loss_percent': round(report['key_transitions']['forest_loss_ha'] / total_area * 100, 2),
        'period_years': year2 - year1
    }
    
    return report


def export_change_map(change_image, aoi, description, folder='EO_Training'):
    """
    Export change detection results to Google Drive
    
    Parameters:
    -----------
    change_image : ee.Image
        Change detection result
    aoi : ee.Geometry
        Area of interest
    description : str
        Export file name
    folder : str
        Google Drive folder
    """
    
    task = ee.batch.Export.image.toDrive(
        image=change_image,
        description=description,
        folder=folder,
        scale=10,
        region=aoi,
        maxPixels=1e13,
        crs='EPSG:4326'
    )
    
    task.start()
    print(f'Export task started: {description}')
    print(f'Check status at: https://code.earthengine.google.com/tasks')


# Utility: Transition matrix table
def create_transition_table(change_matrix, class_names, aoi):
    """
    Create a Pandas DataFrame showing all class transitions
    Useful for detailed change analysis
    
    Returns:
    --------
    pandas.DataFrame : Transition matrix with areas
    """
    
    n_classes = len(class_names)
    transitions = {}
    
    for from_id, from_name in class_names.items():
        transitions[from_name] = {}
        
        for to_id, to_name in class_names.items():
            change_code = from_id * 10 + to_id
            mask = change_matrix.eq(change_code)
            
            area = mask.multiply(ee.Image.pixelArea()).reduceRegion(
                reducer=ee.Reducer.sum(),
                geometry=aoi,
                scale=10,
                maxPixels=1e13
            )
            
            area_ha = ee.Number(area.get('change_code')).divide(10000).getInfo()
            transitions[from_name][to_name] = round(area_ha, 2)
    
    # Convert to DataFrame
    df = pd.DataFrame(transitions).T
    df.index.name = 'From \\ To'
    
    return df
