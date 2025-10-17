# Session 1 Training Data

## Palawan Land Cover Training Polygons

This directory contains training data for supervised classification of Sentinel-2 imagery over Palawan, Philippines.

---

## Files

### `palawan_training_polygons.geojson`
- **Format:** GeoJSON FeatureCollection
- **CRS:** EPSG:4326 (WGS84)
- **Features:** 80 training polygons (10 per class)
- **Attributes:**
  - `class_id`: Numeric class identifier (1-8)
  - `class_name`: Land cover class name
  - `notes`: Additional information

### `palawan_validation_polygons.geojson`
- **Format:** GeoJSON FeatureCollection  
- **Purpose:** Independent validation data
- **Features:** 40 polygons (5 per class)

---

## Land Cover Classification Scheme

| ID | Class Name | Description | Training Samples |
|----|------------|-------------|------------------|
| 1 | Primary Forest | Dense, mature forest canopy | 10 |
| 2 | Secondary Forest | Regenerating forest, lower canopy | 10 |
| 3 | Mangroves | Coastal mangrove forests | 10 |
| 4 | Agricultural Land | Rice paddies, coconut plantations | 10 |
| 5 | Grassland/Scrubland | Open grasslands, sparse vegetation | 10 |
| 6 | Water Bodies | Rivers, lakes, coastal waters | 10 |
| 7 | Urban/Built-up | Settlements, roads, infrastructure | 10 |
| 8 | Bare Soil/Mining | Exposed soil, mining areas | 10 |

---

## Study Area

**Location:** Palawan Province, Philippines  
**Bounding Box:** 
- North: 11.5°N
- South: 8.5°N
- East: 120.5°E
- West: 117.5°E

**Focus Area:** Palawan Biosphere Reserve and surrounding regions

---

## Data Collection Protocol

### Selection Criteria
1. **Homogeneous:** Polygons represent pure class samples
2. **Distributed:** Cover geographic extent of study area
3. **Representative:** Include class variability
4. **Accessible:** Verifiable via high-resolution imagery

### Polygon Size
- Minimum: 50m × 50m (25 Sentinel-2 pixels @ 10m)
- Typical: 100m × 100m to 200m × 200m
- Large features: Up to 500m × 500m

### Reference Data Sources
- Google Earth high-resolution imagery
- Sentinel-2 RGB composites
- Local knowledge and field surveys
- Existing land cover products (ESRI 2020)

---

## Usage in Google Earth Engine

```python
import ee
import geemap

# Initialize Earth Engine
ee.Initialize()

# Load training polygons
training_fc = geemap.geojson_to_ee('palawan_training_polygons.geojson')

# Sample Sentinel-2 data
sentinel = ee.ImageCollection('COPERNICUS/S2_SR') \
    .filterDate('2024-01-01', '2024-12-31') \
    .filterBounds(training_fc) \
    .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 20))

# Create composite
composite = sentinel.median()

# Sample training data
training = composite.sampleRegions(
    collection=training_fc,
    properties=['class_id'],
    scale=10
)

# Train Random Forest classifier
classifier = ee.Classifier.smileRandomForest(100).train(
    features=training,
    classProperty='class_id',
    inputProperties=composite.bandNames()
)
```

---

## Quality Assurance

### Checks Performed
- ✓ No overlapping polygons
- ✓ All polygons within study area
- ✓ Valid geometry (no self-intersections)
- ✓ Balanced class distribution
- ✓ Minimum size requirements met

### Validation
- Independent validation set (40 polygons)
- Stratified random sampling
- Spatial separation from training data

---

## Updates and Maintenance

**Version:** 1.0  
**Last Updated:** October 2025  
**Created By:** CoPhil Training Team

### Change Log
- 2025-10: Initial creation for Day 2 Session 1

### Future Updates
- Add more training samples if accuracy < 80%
- Include seasonal variations
- Expand to other Philippine regions

---

## License and Attribution

**License:** CC-BY-4.0  
**Attribution:** CoPhil Programme, EU-Philippines Copernicus Capacity Support

**Recommended Citation:**
```
CoPhil Programme (2025). Palawan Land Cover Training Data for Sentinel-2 Classification. 
EU-Philippines Copernicus Capacity Support Programme.
```

---

## Contact

For questions or issues with this dataset:
- Review notebook documentation
- Check Session 1 instructor notes
- Consult GEE community forums

---

## References

- Karra et al. (2021). Global land use/land cover with Sentinel-2 and deep learning. IGARSS 2021.
- Stehman, S. V. (1997). Selecting and interpreting measures of thematic classification accuracy.
- Google Earth Engine Classification Guide: https://developers.google.com/earth-engine/guides/classification
