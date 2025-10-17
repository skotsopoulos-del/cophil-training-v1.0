"""
Temporal Composite Template for Google Earth Engine
Multi-temporal Sentinel-2 compositing for land cover classification

Usage: Copy and adapt these functions for your Session 2 notebook
"""

import ee

def create_seasonal_composite(aoi, year, season='dry', cloud_threshold=20):
    """
    Create seasonal Sentinel-2 composite
    
    Parameters:
    -----------
    aoi : ee.Geometry
        Area of interest
    year : int
        Year to process (e.g., 2024)
    season : str
        'dry' (Jan-May) or 'wet' (Jun-Nov)
    cloud_threshold : int
        Maximum cloud percentage (default: 20)
    
    Returns:
    --------
    ee.Image : Seasonal median composite
    """
    
    # Define seasonal date ranges
    if season == 'dry':
        start_date = f'{year}-01-01'
        end_date = f'{year}-05-31'
    elif season == 'wet':
        start_date = f'{year}-06-01'
        end_date = f'{year}-11-30'
    else:
        raise ValueError("Season must be 'dry' or 'wet'")
    
    # Load and filter Sentinel-2
    collection = ee.ImageCollection('COPERNICUS/S2_SR') \
        .filterBounds(aoi) \
        .filterDate(start_date, end_date) \
        .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', cloud_threshold))
    
    # Apply cloud masking
    def mask_clouds(image):
        qa = image.select('QA60')
        cloud_mask = qa.bitwiseAnd(1 << 10).eq(0).And(
                     qa.bitwiseAnd(1 << 11).eq(0))
        return image.updateMask(cloud_mask).divide(10000)
    
    # Create composite
    composite = collection.map(mask_clouds).median()
    
    return composite.clip(aoi)


def create_phenology_composites(aoi, year):
    """
    Create dry and wet season composites for phenological analysis
    
    Returns:
    --------
    dict : {'dry': ee.Image, 'wet': ee.Image}
    """
    
    dry = create_seasonal_composite(aoi, year, season='dry')
    wet = create_seasonal_composite(aoi, year, season='wet')
    
    return {'dry': dry, 'wet': wet}


def add_seasonal_features(dry_composite, wet_composite):
    """
    Derive features from seasonal composites
    
    Parameters:
    -----------
    dry_composite : ee.Image
        Dry season composite
    wet_composite : ee.Image
        Wet season composite
    
    Returns:
    --------
    ee.Image with seasonal features
    """
    
    # NDVI for both seasons
    def calculate_ndvi(image):
        return image.normalizedDifference(['B8', 'B4']).rename('NDVI')
    
    ndvi_dry = calculate_ndvi(dry_composite).rename('NDVI_dry')
    ndvi_wet = calculate_ndvi(wet_composite).rename('NDVI_wet')
    
    # NDVI difference (phenological signal)
    ndvi_diff = ndvi_wet.subtract(ndvi_dry).rename('NDVI_diff')
    
    # NDVI mean
    ndvi_mean = ndvi_dry.add(ndvi_wet).divide(2).rename('NDVI_mean')
    
    # NDWI for water detection
    def calculate_ndwi(image):
        return image.normalizedDifference(['B3', 'B8']).rename('NDWI')
    
    ndwi_dry = calculate_ndwi(dry_composite).rename('NDWI_dry')
    ndwi_wet = calculate_ndwi(wet_composite).rename('NDWI_wet')
    
    # Stack all seasonal features
    seasonal_features = ee.Image.cat([
        dry_composite.select(['B2', 'B3', 'B4', 'B8', 'B11', 'B12']),
        ndvi_dry,
        ndwi_dry,
        ndvi_wet,
        ndwi_wet,
        ndvi_diff,
        ndvi_mean
    ])
    
    return seasonal_features


def create_multi_year_stack(aoi, years, season='dry'):
    """
    Create multi-year temporal stack
    Useful for change detection
    
    Parameters:
    -----------
    aoi : ee.Geometry
        Area of interest
    years : list
        List of years (e.g., [2020, 2021, 2022, 2023, 2024])
    season : str
        Season to composite
    
    Returns:
    --------
    ee.Image with bands from multiple years
    """
    
    composites = []
    
    for year in years:
        composite = create_seasonal_composite(aoi, year, season=season)
        
        # Rename bands to include year
        renamed = composite.select(
            ['B2', 'B3', 'B4', 'B8', 'B11', 'B12'],
            [f'B2_{year}', f'B3_{year}', f'B4_{year}', 
             f'B8_{year}', f'B11_{year}', f'B12_{year}']
        )
        
        composites.append(renamed)
    
    # Stack all years
    multi_year_stack = ee.Image.cat(composites)
    
    return multi_year_stack


def calculate_temporal_metrics(aoi, year, months=12):
    """
    Calculate temporal metrics from monthly composites
    
    Metrics:
    - Mean: Average reflectance
    - StdDev: Temporal variability
    - Min/Max: Range
    - Percentiles: 25th, 75th
    
    Returns:
    --------
    ee.Image with temporal metrics
    """
    
    # Create monthly composites
    start_date = f'{year}-01-01'
    end_date = f'{year}-12-31'
    
    collection = ee.ImageCollection('COPERNICUS/S2_SR') \
        .filterBounds(aoi) \
        .filterDate(start_date, end_date) \
        .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 30)) \
        .select(['B4', 'B8', 'B11'])
    
    # Apply cloud masking
    def mask_clouds(image):
        qa = image.select('QA60')
        mask = qa.bitwiseAnd(1 << 10).eq(0).And(qa.bitwiseAnd(1 << 11).eq(0))
        return image.updateMask(mask).divide(10000)
    
    masked = collection.map(mask_clouds)
    
    # Calculate metrics
    temporal_mean = masked.mean().rename(['B4_mean', 'B8_mean', 'B11_mean'])
    temporal_std = masked.reduce(ee.Reducer.stdDev()).rename(['B4_std', 'B8_std', 'B11_std'])
    temporal_min = masked.min().rename(['B4_min', 'B8_min', 'B11_min'])
    temporal_max = masked.max().rename(['B4_max', 'B8_max', 'B11_max'])
    
    # Stack metrics
    temporal_metrics = ee.Image.cat([
        temporal_mean,
        temporal_std,
        temporal_min,
        temporal_max
    ])
    
    return temporal_metrics.clip(aoi)


# Example usage
def example_palawan_workflow():
    """
    Example: Create seasonal features for Palawan classification
    """
    
    # Define Palawan study area
    palawan = ee.Geometry.Rectangle([118.5, 9.5, 119.5, 10.5])
    
    # Create 2024 seasonal composites
    composites_2024 = create_phenology_composites(palawan, 2024)
    
    # Add seasonal features
    seasonal_features = add_seasonal_features(
        composites_2024['dry'],
        composites_2024['wet']
    )
    
    # Print band names
    print('Seasonal feature bands:', seasonal_features.bandNames().getInfo())
    
    return seasonal_features


# Best practices and tips
"""
TEMPORAL COMPOSITE BEST PRACTICES:

1. SEASON SELECTION:
   Philippines Seasons:
   - Dry: December-May (best for forest mapping)
   - Wet: June-November (good for agriculture, water extent)
   - Transition months: June, November (variable)

2. CLOUD HANDLING:
   - Use QA60 band for cloud masking
   - Set cloud threshold based on data availability
   - Dry season: Can use stricter threshold (10-15%)
   - Wet season: May need to relax (20-30%)
   - Use median() reducer to handle remaining clouds

3. TEMPORAL FEATURES FOR CLASSIFICATION:
   Most Useful:
   - Dry season NDVI: Forest structure
   - Wet season NDVI: Agricultural phenology
   - NDVI difference: Seasonal crops vs perennial
   - NDWI wet season: Maximum water extent
   
4. WHEN TO USE MULTI-TEMPORAL:
   ✓ Separating crops from natural vegetation
   ✓ Identifying seasonal wetlands
   ✓ Detecting irrigated agriculture
   ✓ Monitoring phenological cycles
   
5. COMPUTATIONAL OPTIMIZATION:
   - Create composites first, then derive indices
   - Use .aside(ee.List()) to track progress
   - Export composites for reuse
   - Limit spatial extent during testing

6. CHANGE DETECTION TIPS:
   - Use same season for multi-year comparison
   - Align seasons by month, not calendar year
   - Account for inter-annual climate variability
   - Validate with known change areas

7. COMMON ISSUES:
   - No images available: Adjust date range or cloud threshold
   - Striping: Use median instead of mean
   - Cloud artifacts: Improve cloud masking
   - Seasonal mismatch: Check date ranges

8. FEATURE SELECTION:
   For 8-class Palawan classification, recommended features:
   - Dry season: B2, B3, B4, B8, B11, B12, NDVI, NDWI
   - Wet season: NDVI, NDWI
   - Temporal: NDVI_diff, NDVI_mean
   Total: ~12-15 bands (manageable for Random Forest)
"""

# Advanced: Harmonic regression for time series
def fit_harmonic_trend(aoi, start_year, end_year, band='NDVI'):
    """
    Fit harmonic regression to capture seasonal and trend components
    Useful for detecting gradual changes
    
    WARNING: Computationally intensive for large areas
    """
    
    # Create image collection
    start_date = f'{start_year}-01-01'
    end_date = f'{end_year}-12-31'
    
    # Load and process Sentinel-2
    def add_time_bands(image):
        date = ee.Date(image.get('system:time_start'))
        years = date.difference(ee.Date(start_date), 'year')
        
        # Time in years
        t = ee.Image(years).rename('t').float()
        
        # Harmonic terms
        omega = 2.0 * 3.14159
        cos = t.multiply(omega).cos().rename('cos')
        sin = t.multiply(omega).sin().rename('sin')
        
        return image.addBands([t, cos, sin])
    
    collection = ee.ImageCollection('COPERNICUS/S2_SR') \
        .filterBounds(aoi) \
        .filterDate(start_date, end_date) \
        .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 30)) \
        .map(lambda img: img.normalizedDifference(['B8', 'B4']).rename('NDVI')) \
        .map(add_time_bands)
    
    # Fit linear regression with harmonic terms
    independents = ee.List(['constant', 't', 'cos', 'sin'])
    dependent = ee.String('NDVI')
    
    trend = collection.select(independents.add(dependent)) \
        .reduce(ee.Reducer.linearRegression(independents.length(), 1))
    
    return trend.clip(aoi)
