---
title: "Day 3 Data Acquisition Guide"
subtitle: "Obtaining Real Sentinel Data for Flood Mapping and Object Detection"
format: html
---

## Overview

This guide provides step-by-step instructions for acquiring real Sentinel-1 SAR and Sentinel-2 optical data for the Day 3 exercises. The training materials use pre-processed datasets, but this guide helps you work with production data for your own projects.

## Sentinel-1 SAR Data for Flood Mapping

### Data Requirements
- **Mission:** Sentinel-1A/1B
- **Product Type:** GRD (Ground Range Detected)
- **Polarization:** VV, VH
- **Resolution:** 10m
- **Processing Level:** Level-1

### Access Methods

#### 1. Copernicus Data Space Ecosystem

1. Visit [Copernicus Data Space](https://dataspace.copernicus.eu/)
2. Create a free account
3. Use the Browser to search for Sentinel-1 GRD products
4. Filter by:
   - Geographic area (e.g., Central Luzon, Philippines)
   - Date range (before/after flood event)
   - Polarization (VV+VH preferred)
5. Download products directly or use the API

#### 2. Google Earth Engine

```javascript
// Load Sentinel-1 SAR data
var s1 = ee.ImageCollection('COPERNICUS/S1_GRD')
  .filterBounds(roi)
  .filterDate('2023-07-01', '2023-07-31')
  .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV'))
  .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VH'))
  .filter(ee.Filter.eq('instrumentMode', 'IW'))
  .select(['VV', 'VH']);

// Get before and after images
var before = s1.filterDate('2023-07-01', '2023-07-15').median();
var after = s1.filterDate('2023-07-20', '2023-07-31').median();

// Export to Drive
Export.image.toDrive({
  image: before,
  description: 'S1_before_flood',
  scale: 10,
  region: roi,
  maxPixels: 1e13
});
```

#### 3. PhilSA SIYASAT Portal

For Philippine-specific data:
1. Visit [SIYASAT](https://siyasat.philsa.gov.ph/)
2. Search for Sentinel-1 data over your area of interest
3. Download preprocessed products when available

## Sentinel-2 Optical Data for Object Detection

### Data Requirements
- **Mission:** Sentinel-2A/2B
- **Product Type:** L2A (Bottom of Atmosphere)
- **Bands:** True color (B4, B3, B2) + NIR (B8)
- **Resolution:** 10m
- **Cloud Cover:** < 10%

### Access Methods

#### 1. Copernicus Data Space Ecosystem

1. Search for Sentinel-2 L2A products
2. Filter by:
   - Area of interest (e.g., Metro Manila)
   - Cloud cover percentage
   - Date range
3. Preview images before downloading
4. Download specific bands or entire tile

#### 2. Google Earth Engine

```javascript
// Load Sentinel-2 Surface Reflectance
var s2 = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
  .filterBounds(roi)
  .filterDate('2024-01-01', '2024-12-31')
  .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10))
  .select(['B4', 'B3', 'B2', 'B8']);

// Get median composite
var composite = s2.median();

// Export high-resolution image
Export.image.toDrive({
  image: composite,
  description: 'S2_Metro_Manila',
  scale: 10,
  region: roi,
  maxPixels: 1e13
});
```

## Preprocessing Steps

### For Flood Mapping (Sentinel-1)

1. **Speckle Filtering:** Apply Lee or Refined Lee filter
2. **Radiometric Calibration:** Convert to sigma0 in dB
3. **Terrain Correction:** Use SRTM DEM
4. **Normalization:** Scale to 0-1 range for model input

### For Object Detection (Sentinel-2)

1. **Atmospheric Correction:** Use L2A products (already corrected)
2. **Band Selection:** RGB + NIR bands
3. **Cloud Masking:** Remove cloudy pixels
4. **Normalization:** Scale to 0-1 range
5. **Tiling:** Create 256×256 or 512×512 tiles for training

## Annotation Tools

### For Flood Extent Mapping

- **QGIS:** Free GIS software for manual polygon digitization
- **Label Studio:** Web-based annotation platform
- **Google Earth Engine Code Editor:** Interactive labeling

### For Object Detection

- **LabelImg:** Desktop tool for bounding box annotation
- **CVAT:** Web-based Computer Vision Annotation Tool
- **Roboflow:** Cloud platform with labeling and dataset management

## Philippine-Specific Datasets

### Pre-annotated Datasets

1. **PhilSA Data Portal:** Check for available labeled datasets
2. **DOST-ASTI:** Contact for research collaboration
3. **CoPhil Programme:** Access training datasets from course materials

### Recommended Study Areas

**Flood Mapping:**
- Pampanga River Basin (Central Luzon)
- Cagayan River Basin (Cagayan Valley)
- Agusan River Basin (Mindanao)

**Urban Object Detection:**
- Metro Manila (NCR)
- Metro Cebu (Central Visayas)
- Metro Davao (Davao Region)

## Data Processing Workflows

### Python Workflow Example

```python
import rasterio
from rasterio.plot import show
import numpy as np

# Read Sentinel-1 GRD
with rasterio.open('S1_GRD.tif') as src:
    vv = src.read(1)
    vh = src.read(2)

# Convert to dB
vv_db = 10 * np.log10(vv + 1e-10)
vh_db = 10 * np.log10(vh + 1e-10)

# Normalize for model input
vv_norm = (vv_db + 30) / 30  # Assuming -30 to 0 dB range
vh_norm = (vh_db + 30) / 30

# Stack bands
input_data = np.stack([vv_norm, vh_norm], axis=-1)
```

## Additional Resources

### Documentation
- [Sentinel-1 User Guide](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-1-sar)
- [Sentinel-2 User Guide](https://sentinel.esa.int/web/sentinel/user-guides/sentinel-2-msi)
- [Google Earth Engine Guides](https://developers.google.com/earth-engine/guides)

### Philippine EO Resources
- [PhilSA Official Website](https://philsa.gov.ph/)
- [NAMRIA Geoportal](https://www.namria.gov.ph/)
- [PAGASA Weather Data](https://www.pagasa.dost.gov.ph/)

### Support
For questions about data acquisition:
- CoPhil Programme support channels
- PhilSA technical support
- ESA Copernicus user forum

---

*This guide is part of the CoPhil EO AI/ML Training Programme - Day 3: Advanced Deep Learning for Earth Observation*
