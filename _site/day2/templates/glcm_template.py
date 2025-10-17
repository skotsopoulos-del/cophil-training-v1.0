"""
GLCM Texture Feature Template for Google Earth Engine
Gray-Level Co-occurrence Matrix texture features for land cover classification

Usage: Copy and adapt these functions for your Session 2 notebook
"""

import ee

def add_glcm_texture(image, bands=['B8'], radius=1):
    """
    Add GLCM texture features to an image
    
    Parameters:
    -----------
    image : ee.Image
        Input Sentinel-2 image
    bands : list
        Bands to compute texture from (default: NIR band B8)
    radius : int
        Neighborhood radius in pixels (default: 1 = 3x3 window)
    
    Returns:
    --------
    ee.Image with added texture bands
    
    Texture Features:
    - asm: Angular Second Moment (uniformity)
    - contrast: Local variation
    - corr: Correlation between pixel pairs
    - var: Variance
    - idm: Inverse Difference Moment (homogeneity)
    - savg: Sum Average
    - svar: Sum Variance
    - sent: Sum Entropy
    - ent: Entropy (randomness)
    - dvar: Difference Variance
    - dent: Difference Entropy
    - imcorr1, imcorr2: Information Measures of Correlation
    """
    
    # Select band for texture calculation
    gray = image.select(bands)
    
    # Compute GLCM with specified radius
    # size = (radius * 2) + 1
    glcm = gray.glcmTexture(size=radius * 2 + 1)
    
    # Return image with GLCM bands added
    return image.addBands(glcm)


def add_selected_glcm(image, bands=['B8'], features=['contrast', 'ent', 'corr']):
    """
    Add only selected GLCM texture features (faster computation)
    
    Parameters:
    -----------
    image : ee.Image
        Input Sentinel-2 image
    bands : list
        Bands to compute texture from
    features : list
        Which texture features to keep
        Options: 'contrast', 'corr', 'ent', 'var', 'idm', 'asm'
    
    Returns:
    --------
    ee.Image with selected texture bands
    """
    
    # Compute all GLCM features
    glcm = add_glcm_texture(image, bands=bands)
    
    # Build list of band names to select
    texture_bands = []
    for band in bands:
        for feature in features:
            texture_bands.append(f'{band}_{feature}')
    
    # Select only requested features
    selected = glcm.select(texture_bands)
    
    return image.addBands(selected)


def glcm_for_classification(image, nir_band='B8', red_band='B4'):
    """
    Add optimized GLCM features for land cover classification
    Uses NIR for vegetation texture and Red for overall contrast
    
    Parameters:
    -----------
    image : ee.Image
        Input Sentinel-2 image
    nir_band : str
        Near-infrared band name (default: 'B8')
    red_band : str
        Red band name (default: 'B4')
    
    Returns:
    --------
    ee.Image with classification-optimized texture features
    """
    
    # NIR texture (good for vegetation structure)
    nir_texture = image.select(nir_band).glcmTexture(size=3)
    nir_contrast = nir_texture.select(f'{nir_band}_contrast').rename('nir_texture_contrast')
    nir_entropy = nir_texture.select(f'{nir_band}_ent').rename('nir_texture_entropy')
    nir_corr = nir_texture.select(f'{nir_band}_corr').rename('nir_texture_corr')
    
    # Red texture (good for overall image structure)
    red_texture = image.select(red_band).glcmTexture(size=3)
    red_contrast = red_texture.select(f'{red_band}_contrast').rename('red_texture_contrast')
    
    # Combine selected features
    texture_features = ee.Image.cat([
        nir_contrast,
        nir_entropy,
        nir_corr,
        red_contrast
    ])
    
    return image.addBands(texture_features)


# Example usage in GEE workflow
def example_usage():
    """
    Example: Add texture features to Sentinel-2 image
    """
    
    # Define area of interest (Palawan example)
    aoi = ee.Geometry.Rectangle([118.5, 9.5, 119.5, 10.5])
    
    # Load Sentinel-2 image
    s2 = ee.ImageCollection('COPERNICUS/S2_SR') \
        .filterBounds(aoi) \
        .filterDate('2024-01-01', '2024-04-30') \
        .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20)) \
        .median()
    
    # Method 1: Add all GLCM features (slow but comprehensive)
    # image_with_all_texture = add_glcm_texture(s2, bands=['B8'], radius=1)
    
    # Method 2: Add selected features (faster)
    image_with_selected = add_selected_glcm(
        s2, 
        bands=['B8'], 
        features=['contrast', 'ent', 'corr']
    )
    
    # Method 3: Add optimized features for classification (recommended)
    image_with_optimized = glcm_for_classification(s2)
    
    # Print band names to verify
    print('Optimized texture bands:', image_with_optimized.bandNames().getInfo())
    
    return image_with_optimized


# Tips for using GLCM in land cover classification:
"""
GLCM TIPS & BEST PRACTICES:

1. COMPUTATIONAL COST:
   - GLCM is computationally expensive
   - Use smaller windows (3x3 or 5x5) for faster processing
   - Select only needed features (contrast, entropy, correlation)
   - Avoid computing on large areas at once

2. WHICH FEATURES TO USE:
   - Contrast: Distinguishes forest from agriculture
   - Entropy: Captures urban heterogeneity
   - Correlation: Good for textured surfaces (forest canopy)
   - Variance: Similar to contrast but different scale
   
3. WHICH BANDS:
   - NIR (B8): Best for vegetation texture
   - Red (B4): Good for overall structure
   - SWIR (B11): Useful for urban/bare soil
   - Avoid using too many bands (slows computation)

4. WINDOW SIZE:
   - 3x3 (radius=1): Good for 10m Sentinel-2
   - 5x5 (radius=2): Captures more context but slower
   - 7x7 (radius=3): Too large for 10m data usually

5. WHEN TO USE:
   - Separating primary vs secondary forest (canopy texture)
   - Urban vs bare soil (heterogeneity)
   - Mangroves vs water (structural complexity)
   
6. WHEN NOT TO USE:
   - Spectral differences are sufficient
   - Time constraints (GLCM is slow)
   - Very heterogeneous landscapes (texture less meaningful)

7. OPTIMIZATION:
   - Compute texture on median composite, not each image
   - Use .aside() to print progress during development
   - Consider pre-computing and exporting for large areas
   - Use .reproject() carefully to avoid memory issues

8. TROUBLESHOOTING:
   - "Computation timed out": Reduce area or window size
   - "Memory limit exceeded": Process in tiles
   - "Too slow": Select fewer features or smaller radius
   - Results look strange: Check band scaling (0-1 vs 0-10000)
"""

# Advanced: Multi-scale texture
def multiscale_glcm(image, band='B8', radii=[1, 2]):
    """
    Compute GLCM at multiple scales
    Useful for capturing texture at different spatial frequencies
    
    WARNING: Very computationally expensive!
    """
    texture_features = []
    
    for radius in radii:
        glcm = image.select(band).glcmTexture(size=radius * 2 + 1)
        
        # Select key features and rename with scale
        contrast = glcm.select(f'{band}_contrast').rename(f'texture_contrast_r{radius}')
        entropy = glcm.select(f'{band}_ent').rename(f'texture_entropy_r{radius}')
        
        texture_features.extend([contrast, entropy])
    
    return image.addBands(texture_features)
