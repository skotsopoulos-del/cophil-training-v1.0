# Palawan Land Cover Classification Scheme

## Overview

This document defines the 8-class land cover classification scheme for Palawan, Philippines, designed for Sentinel-2 imagery analysis using Random Forest classification.

---

## Classification System

### Based on:
- ESRI 2020 Global LULC (Sentinel-2)
- Philippine National Land Cover standards
- Palawan Biosphere Reserve monitoring needs
- Sentinel-2 spectral separability

---

## Class Definitions

### Class 1: Primary Forest
**Code:** `1`  
**Color:** Dark Green (#0A5F0A)

**Description:**
Dense, mature forest with closed canopy cover (>70%). Tall trees (>15m height) with minimal disturbance. Includes old-growth dipterocarp forests characteristic of Palawan.

**Spectral Characteristics:**
- High NIR reflectance
- Low red reflectance
- Very high NDVI (>0.7)
- Low NDBI
- Moderate SWIR absorption

**Typical Locations:**
- Protected areas in northern Palawan
- Central mountain ranges
- Cleopatra's Needle area
- Mount Mantalingajan

**Key Features:**
- Continuous canopy
- No visible clearings
- High biomass density
- Evergreen phenology

---

### Class 2: Secondary Forest
**Code:** `2`  
**Color:** Light Green (#4CAF50)

**Description:**
Regenerating forest with lower canopy height and density. Previously disturbed areas showing forest regrowth. Mix of pioneer and secondary species.

**Spectral Characteristics:**
- Moderate to high NIR
- Moderate NDVI (0.5-0.7)
- More variable texture than primary forest
- Seasonal variation in reflectance

**Typical Locations:**
- Forest edges
- Previously logged areas
- Regenerating clearings
- Buffer zones around settlements

**Key Features:**
- Lower, uneven canopy
- Visible gaps
- Mix of tree ages
- Faster growth rate

---

### Class 3: Mangroves
**Code:** `3`  
**Color:** Teal (#009688)

**Description:**
Coastal mangrove forests in intertidal zones. Salt-tolerant vegetation with distinctive root systems. Critical for coastal protection and fisheries.

**Spectral Characteristics:**
- Very high NIR
- High NDVI (0.6-0.8)
- Very high NDWI (water mixing)
- Unique SWIR signature
- Tidal variation

**Typical Locations:**
- Eastern and western coastlines
- River estuaries
- Honda Bay area
- Coastal protected zones

**Key Features:**
- Water proximity
- Dense vegetation
- Tidal influence
- Characteristic root structure

---

### Class 4: Agricultural Land
**Code:** `4`  
**Color:** Yellow (#FFC107)

**Description:**
Human-cultivated land including rice paddies, coconut plantations, and other crops. Shows regular geometric patterns and seasonal variation.

**Spectral Characteristics:**
- Highly variable by crop type
- NDVI varies by season (0.3-0.7)
- High NDWI during rice growing
- Geometric patterns visible
- Bare soil between seasons

**Typical Locations:**
- Coastal plains
- River valleys
- Around settlements
- Flat to gently sloping areas

**Key Features:**
- Regular field patterns
- Seasonal changes
- Irrigation infrastructure
- Mix of crop types

**Sub-types:**
- Rice paddies (flooded agriculture)
- Coconut plantations
- Mixed crops
- Fallow fields

---

### Class 5: Grassland/Scrubland
**Code:** `5`  
**Color:** Light Yellow (#FFEB3B)

**Description:**
Open areas with grass, shrubs, and sparse vegetation. Includes natural savannas and degraded forest lands. Lower vegetation height than forests.

**Spectral Characteristics:**
- Moderate NDVI (0.3-0.5)
- High red and NIR mix
- Seasonal browning in dry season
- Low canopy cover
- Visible soil

**Typical Locations:**
- Grassland savannas
- Degraded forest areas
- Upland pastures
- Rocky hillsides

**Key Features:**
- Low vegetation
- Seasonal color change
- Exposed soil patches
- Sparse tree cover (<10%)

---

### Class 6: Water Bodies
**Code:** `6`  
**Color:** Blue (#2196F3)

**Description:**
Permanent and seasonal water including rivers, lakes, ponds, and coastal waters. Clear to turbid water bodies.

**Spectral Characteristics:**
- Very low NIR
- Negative or very low NDVI
- Very high NDWI (>0.3)
- High blue and green reflectance
- Low SWIR reflectance

**Typical Locations:**
- Rivers and streams
- Lakes and ponds
- Coastal waters
- Reservoirs

**Key Features:**
- Low vegetation
- Smooth texture
- Seasonal extent variation
- Sediment load variation

**Sub-types:**
- Clear water (low sediment)
- Turbid water (high sediment)
- Shallow water (bottom visible)
- Deep water

---

### Class 7: Urban/Built-up
**Code:** `7`  
**Color:** Red (#F44336)

**Description:**
Human-built structures including buildings, roads, and paved areas. Impervious surfaces with high reflectance.

**Spectral Characteristics:**
- High reflectance in all bands
- Very low NDVI (<0.2)
- High NDBI (>0.1)
- High SWIR reflectance
- Bright, heterogeneous

**Typical Locations:**
- Puerto Princesa City
- Towns and villages
- Road networks
- Port facilities

**Key Features:**
- Impervious surfaces
- Geometric patterns
- High density structures
- Roads and buildings

**Sub-types:**
- Dense urban (city center)
- Residential areas
- Commercial zones
- Roads and infrastructure

---

### Class 8: Bare Soil/Mining
**Code:** `8`  
**Color:** Brown (#795548)

**Description:**
Exposed soil, rock, and mining areas. Minimal vegetation cover. Includes natural bare areas and human-disturbed sites.

**Spectral Characteristics:**
- Very low NDVI (<0.2)
- High red and SWIR
- Bright in all bands
- No vegetation signal
- Smooth or rough texture

**Typical Locations:**
- Mining sites
- Construction areas
- Eroded hillsides
- Quarries
- Beaches (non-coastal water)

**Key Features:**
- No vegetation
- Exposed substrate
- Often disturbed
- Variable color/brightness

**Sub-types:**
- Active mining
- Cleared land
- Natural bare rock
- Eroded areas

---

## Spectral Index Summary

| Class | NDVI Range | NDWI Range | NDBI Range | NIR Character |
|-------|-----------|-----------|-----------|--------------|
| 1. Primary Forest | 0.7-0.9 | -0.2-0.1 | -0.3--0.2 | Very High |
| 2. Secondary Forest | 0.5-0.7 | -0.1-0.1 | -0.2--0.1 | High |
| 3. Mangroves | 0.6-0.8 | 0.2-0.5 | -0.3--0.2 | Very High |
| 4. Agricultural | 0.3-0.7 | -0.1-0.3 | -0.2-0.1 | Variable |
| 5. Grassland | 0.3-0.5 | -0.2-0.0 | -0.1-0.1 | Moderate |
| 6. Water | <0.1 | >0.3 | -0.4--0.3 | Very Low |
| 7. Urban | <0.2 | <0.0 | >0.1 | Low |
| 8. Bare Soil | <0.2 | <0.0 | 0.0-0.2 | Very Low |

---

## Class Confusion Matrix (Expected)

Common misclassifications to watch for:

| Confused Classes | Reason | Mitigation |
|-----------------|--------|-----------|
| Primary ↔ Secondary Forest | Canopy density gradient | Use texture features, multi-temporal |
| Mangroves ↔ Flooded Agriculture | Water mixing | Use tidal timing, SWIR bands |
| Grassland ↔ Bare Soil | Dry season similarity | Use seasonal composites |
| Urban ↔ Bare Soil | Bright surfaces | Use geometric patterns, NDBI |
| Secondary Forest ↔ Agriculture | Similar NDVI | Use field patterns, temporal |

---

## Seasonal Considerations

### Dry Season (December - May)
- Grasslands appear brown/yellow
- Agricultural fields may be bare
- Rivers show lower water extent
- Best for forest classification

### Wet Season (June - November)
- Agricultural fields green/flooded
- Maximum water extent
- Cloud cover challenging
- Good for mangrove delineation

### Recommended Composite
Use **dry season** (January-April) for primary classification, supplemented with wet season (July-September) for agriculture and water.

---

## Training Sample Requirements

### Minimum per Class
- **Training:** 50-100 pixels per class
- **Validation:** 30-50 pixels per class
- **Total:** 10 polygons × 8 classes = 80 training polygons

### Sample Distribution
- Geographic spread across study area
- Include class variability
- Avoid edges and mixed pixels
- Reference high-resolution imagery

---

## References

1. Karra et al. (2021). Global land use/land cover with Sentinel-2 and deep learning. IGARSS 2021.
2. ESRI 2020 Land Cover Classification Scheme
3. Philippine Forestry Statistics (DENR)
4. Palawan Biosphere Reserve Management Plan
5. Sentinel-2 User Handbook (ESA)

---

## Version History

- **v1.0** (Oct 2025): Initial classification scheme for CoPhil training
- Based on pilot testing with Session 1 materials
- Optimized for Sentinel-2 10m bands + indices

---

## Usage Notes

### For Instructors
- Emphasize spectral separability
- Discuss confusion between similar classes
- Show example spectra for each class
- Relate to Philippine context

### For Students
- Study class characteristics carefully
- Understand spectral index ranges
- Consider seasonal effects
- Practice identifying classes in imagery

### For Future Updates
- Add more sub-classes if needed
- Refine based on accuracy assessment
- Include seasonal variants
- Expand to other Philippine regions
