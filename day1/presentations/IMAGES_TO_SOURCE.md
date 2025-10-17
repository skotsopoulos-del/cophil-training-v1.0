# Images to Source - Priority List

**Save all images to:** `course_site/day1/presentations/images/`

---

## 🔴 CRITICAL - Source These First (30 minutes)

### **1. Official Logos (Download from websites)**

| Filename | Source | How to Get |
|----------|--------|------------|
| `philsa_logo.png` | [PhilSA](https://philsa.gov.ph) | Right-click logo → Save image as... |
| `dost_logo.png` | [DOST](https://www.dost.gov.ph) | Footer or header logo |
| `dost_asti_logo.png` | [DOST-ASTI](https://asti.dost.gov.ph) | Header logo |
| `namria_logo.png` | [NAMRIA](https://www.namria.gov.ph) | Header logo |
| `gee_logo.png` | [Google Earth Engine](https://earthengine.google.com) | Homepage or press kit |
| `copphil_logo.png` | CoPhil materials | If you have CoPhil branding materials |
| `eu_global_gateway.png` | [EU Website](https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/stronger-europe-world/global-gateway_en) | Logo/banner image |

**Tips:**
- Look for PNG format with transparent background
- Save as high resolution (at least 400x400px for logos)
- Check website footer for "Media" or "Downloads" sections

---

### **2. Sentinel Satellite Images (ESA Official)**

| Filename | Source | How to Get |
|----------|--------|------------|
| `sentinel1_satellite.jpg` | [ESA Multimedia](https://www.esa.int/ESA_Multimedia/Search?SearchText=sentinel-1+satellite&result_type=images) | Search "Sentinel-1 satellite" → Download high-res |
| `sentinel2_mayon.jpg` | [Copernicus Browser](https://dataspace.copernicus.eu) | Navigate to Mayon Volcano (13.26°N, 123.69°E), Sentinel-2, true color → Screenshot |

**For Copernicus Browser:**
1. Go to https://dataspace.copernicus.eu/browser/
2. Search location or coordinates
3. Select Sentinel-2 L2A
4. Choose date with <10% cloud cover
5. Select "True Color" visualization
6. Take screenshot (full screen for best quality)

---

### **3. Philippine Platform Screenshots (15 minutes)**

| Filename | URL to Screenshot | What to Capture |
|----------|-------------------|-----------------|
| `siyasat_portal.jpg` | Contact PhilSA or search online | SIYASAT platform interface |
| `namria_geoportal.jpg` | [NAMRIA Geoportal](https://www.geoportal.gov.ph) | Homepage or map view |
| `dataspace_portal.jpg` | [Copernicus Data Space](https://dataspace.copernicus.eu) | Homepage or browser interface |

**How to take good screenshots:**
- Use full screen browser (F11)
- Hide browser toolbars
- Capture at 1920x1080 resolution
- Save as JPG or PNG

---

## 🟡 HIGH PRIORITY - Create These Diagrams (2-3 hours)

### **4. Custom Diagrams to Create**

These are critical diagrams you need to create (use PowerPoint, draw.io, or Canva):

#### **A. Philippine EO Ecosystem (`ph_eo_ecosystem.png`)**

Create a diagram showing:
```
┌─────────────────────────────────────────┐
│         EU Copernicus Programme         │
│      (Sentinel-1, Sentinel-2, ...)      │
└────────────────┬────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────┐
│           CoPhil Programme             │
│    (EU-Philippines Cooperation)         │
└─────┬─────────────┬──────────────┬──────┘
      │             │              │
      ▼             ▼              ▼
  ┌────────┐   ┌─────────┐   ┌──────────┐
  │ PhilSA │   │ NAMRIA  │   │DOST-ASTI │
  │SIYASAT │   │Geoportal│   │SkAI-Pinas│
  └────────┘   └─────────┘   └──────────┘
```

**Tools:** draw.io (free), PowerPoint, or Canva
**Size:** 1920x1080px
**Colors:** Use blue (#1e3a8a) as primary color

---

#### **B. EO ML Workflow (`eo_ml_workflow.png`)**

Create a workflow diagram:
```
Problem → Data Collection → Preprocessing → 
Feature Engineering → Model Training → 
Validation → Deployment → Monitoring
```

**Include:**
- Icons or boxes for each step
- Arrows showing flow
- Brief labels under each step
- Feedback loop from Monitoring back to Data Collection

**Size:** 1920x1080px

---

#### **C. Foundation Models Timeline (`foundation_models_timeline.png`)**

Create a timeline showing:
```
2023: Early EO foundation models
  │
2024: NASA-IBM Geospatial FM (Aug)
  │   ESA Φsat-2 launched (Sept)
  │
2025: Prithvi, Clay models released
  │
Future: Widespread adoption
```

**Style:** Horizontal timeline with key milestones
**Size:** 1920x1080px

---

#### **D. Python Geospatial Stack (`python_geospatial_stack.png`)**

Create a diagram showing Python libraries:
```
┌───────────────────────────────────┐
│   Application Layer               │
│   (Your Analysis Code)            │
└───────────┬───────────────────────┘
            │
┌───────────┴───────────────────────┐
│   High-Level Libraries            │
│   GeoPandas | Rasterio | geemap   │
└───────────┬───────────────────────┘
            │
┌───────────┴───────────────────────┐
│   Core Libraries                  │
│   GDAL | Shapely | NumPy          │
└───────────────────────────────────┘
```

**Size:** 1600x900px

---

## 🟢 MEDIUM PRIORITY - Good to Have (2-4 hours)

### **5. Example EO Images**

| Filename | How to Create | Description |
|----------|---------------|-------------|
| `s1_flood_mapping.jpg` | Copernicus Browser | Sentinel-1 showing flood extent (dark = water) |
| `sentinel1_flood_ph.png` | Copernicus Browser | Philippine flooding example (recent typhoon) |
| `classification_example.jpg` | Copernicus Browser | Sentinel-2 false color showing land cover types |
| `rice_monitoring_ph.jpg` | Copernicus Browser | Rice fields in Central Luzon (green/brown patches) |

**How to get these:**
1. Go to Copernicus Browser
2. Navigate to Philippine locations
3. Select appropriate satellite and date
4. Choose visualization (True Color, False Color, NDVI)
5. Screenshot at high resolution

---

### **6. Concept Diagrams (Create Simple Versions)**

| Filename | What to Show | Tools |
|----------|--------------|-------|
| `ai_ml_dl_venn.png` | Three overlapping circles: AI (largest), ML (medium), DL (smallest) | PowerPoint circles |
| `supervised_learning_concept.png` | Input data + Labels → Model → Predictions | Simple flowchart |
| `cnn_architecture.png` | Boxes showing: Input Image → Conv → Pool → Conv → Pool → Dense → Output | PowerPoint shapes |
| `random_forest_diagram.png` | Multiple decision trees → Combined prediction | Simple tree diagrams |

**Keep these simple** - don't need to be fancy, just clear!

---

## ⚪ LOW PRIORITY - Can Skip or Use Text Instead

These are nice-to-have but not essential:

- `sar_principle.png` - SAR imaging principle (can explain verbally)
- `polarization_comparison.jpg` - VV vs VH (can show in live demo)
- `philsa_building.jpg` - PhilSA headquarters (not critical)
- `confusion_matrix.png` - Example matrix (can draw on slide)
- Various platform interfaces (can show live instead)

---

## 📥 Quick Download Guide

### **Step-by-Step for ESA Images:**

1. **Visit ESA Multimedia Gallery:**
   https://www.esa.int/ESA_Multimedia/Images

2. **Search terms to use:**
   - "Sentinel-1 satellite"
   - "Sentinel-2 satellite"
   - "Copernicus programme"

3. **Download:**
   - Click image → "Download" button
   - Choose high resolution
   - Save to `images/` folder

4. **Rename:**
   - Rename downloaded file to match required filename
   - Example: `ESA_Sentinel1.jpg` → `sentinel1_satellite.jpg`

---

### **Step-by-Step for Copernicus Browser Images:**

1. **Open Copernicus Browser:**
   https://dataspace.copernicus.eu/browser/

2. **For Mayon Volcano example:**
   - Search: "Mayon Volcano" or coordinates (13.26°N, 123.69°E)
   - Select: Sentinel-2 L2A
   - Date: Any recent date with <20% cloud
   - Visualization: True Color (B4-B3-B2)
   - Zoom in to fill frame
   - Take screenshot

3. **For Flood example:**
   - Navigate to recently flooded area in Philippines
   - Select: Sentinel-1 GRD IW
   - Date: During flood event
   - Visualization: VV polarization
   - Dark areas = water
   - Take screenshot showing contrast

4. **For Rice monitoring:**
   - Navigate to Central Luzon (Nueva Ecija area)
   - Select: Sentinel-2 L2A
   - Date: Growing season (June-October)
   - Visualization: False Color (B8-B4-B3) or NDVI
   - Rice fields appear bright red (healthy) or brown (harvested)
   - Take screenshot

---

## 🎨 Creating Diagrams - Quick Tips

### **Using PowerPoint/Google Slides:**

1. **Set slide size to 1920x1080:**
   - File → Page Setup → Custom (1920 x 1080)

2. **Use simple shapes:**
   - Insert → Shapes → Rectangles, circles, arrows
   - Add text boxes for labels

3. **Color scheme:**
   - Primary: Blue #1e3a8a
   - Background: White or light gray #f3f4f6
   - Text: Dark gray #1f2937

4. **Export:**
   - File → Save As → PNG or JPG
   - Maximum resolution

### **Using draw.io (Free Online Tool):**

1. **Go to:** https://app.diagrams.net

2. **Create new diagram:**
   - Choose blank diagram
   - Set canvas size: File → Page Setup → Custom (1920x1080)

3. **Drag and drop:**
   - Shapes from left sidebar
   - Connect with arrows
   - Add text labels

4. **Export:**
   - File → Export As → PNG
   - Select high resolution
   - Transparent background: optional

---

## ✅ Checklist - Track Your Progress

As you source images, check them off:

### **Critical (30-60 minutes):**
- [ ] philsa_logo.png
- [ ] dost_logo.png
- [ ] dost_asti_logo.png
- [ ] namria_logo.png
- [ ] gee_logo.png
- [ ] sentinel1_satellite.jpg
- [ ] sentinel2_mayon.jpg (or any S2 image)
- [ ] dataspace_portal.jpg (screenshot)

### **High Priority (2-3 hours):**
- [ ] ph_eo_ecosystem.png (CREATE diagram)
- [ ] eo_ml_workflow.png (CREATE diagram)
- [ ] foundation_models_timeline.png (CREATE diagram)
- [ ] python_geospatial_stack.png (CREATE diagram)

### **Medium Priority (2-4 hours):**
- [ ] siyasat_portal.jpg (if accessible)
- [ ] namria_geoportal.jpg (screenshot)
- [ ] s1_flood_mapping.jpg (Copernicus Browser)
- [ ] classification_example.jpg (Copernicus Browser)
- [ ] ai_ml_dl_venn.png (CREATE simple)
- [ ] cnn_architecture.png (CREATE simple)

### **Low Priority (optional):**
- [ ] Everything else can wait or be skipped

---

## 📊 Time Estimate

| Task | Time | Files |
|------|------|-------|
| **Download logos** | 30 min | 7 logos |
| **ESA satellite images** | 15 min | 2 images |
| **Platform screenshots** | 15 min | 3 screenshots |
| **Create 4 key diagrams** | 2-3 hours | 4 diagrams |
| **Create example EO images** | 1 hour | 4 images |
| **Create simple concept diagrams** | 1-2 hours | 4 diagrams |
| **TOTAL (Essential)** | **3-4 hours** | **20 images** |
| **TOTAL (All high priority)** | **4-6 hours** | **24 images** |

---

## 🚀 Recommended Workflow

**Today (1 hour):**
1. Download all logos (30 min)
2. Download ESA satellite images (15 min)
3. Screenshot key platforms (15 min)
4. **Result:** Presentations 50% better visually

**Tomorrow (2-3 hours):**
1. Create Philippine EO ecosystem diagram (45 min)
2. Create EO ML workflow diagram (45 min)
3. Create foundation models timeline (30 min)
4. Create Python stack diagram (30 min)
5. **Result:** Presentations 80% complete visually

**Later (optional, 2-4 hours):**
1. Create example EO images from Copernicus Browser
2. Create simple concept diagrams
3. Source remaining platform screenshots
4. **Result:** Presentations 100% complete

---

## 📞 Need Help?

**Can't find a specific image?**
- Skip it and use text-based slide instead
- Show live demo during presentation
- Use placeholder and explain verbally

**Don't have time for diagrams?**
- Use text bullet points instead
- Draw on screen during presentation
- Use whiteboard/annotation tools

**Questions about which images matter most?**
- Logos are most important (credibility)
- Diagrams are second (understanding)
- Examples are third (engagement)
- Everything else is optional

---

## 📁 Final Check

After sourcing images:

```bash
cd course_site/day1/presentations/images

# Check you have the critical files:
ls -lh philsa_logo.png dost_logo.png gee_logo.png \
       sentinel1_satellite.jpg ph_eo_ecosystem.png \
       eo_ml_workflow.png

# Re-render presentations:
cd ..
quarto render 01_session1_copernicus_philippine_eo.qmd
quarto render 02_session2_ai_ml_fundamentals.qmd

# Preview to check:
quarto preview 01_session1_copernicus_philippine_eo.qmd
```

**Good luck! Start with the critical items and you'll have great-looking presentations! 🚀**
