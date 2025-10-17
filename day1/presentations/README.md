# Day 1 Presentations - User Guide

**CoPhil EO AI/ML Training Programme**  
**EU-Philippines Copernicus Capacity Support**

---

## 📚 Contents

This directory contains all presentation materials for Day 1 of the training:

| File | Purpose | Duration |
|------|---------|----------|
| `00_precourse_orientation.qmd` | Pre-course setup & orientation | 45-60 min |
| `01_session1_copernicus_philippine_eo.qmd` | Copernicus & Philippine EO ecosystem | 120 min |
| `02_session2_ai_ml_fundamentals.qmd` | AI/ML concepts for Earth Observation | 120 min |
| `03_session3_python_geospatial.qmd` | Python geospatial analysis (hands-on) | 120 min |
| `04_session4_google_earth_engine.qmd` | Google Earth Engine with Python | 120 min |
| `custom.scss` | Custom styling (minimal & clean) | - |
| `INSTRUCTOR_GUIDE.md` | Comprehensive teaching guide | - |
| `IMPLEMENTATION_STATUS.md` | Development progress tracker | - |
| `ENHANCEMENT_SUMMARY.md` | Enhancement framework documentation | - |

---

## 🚀 Quick Start

### **Rendering Presentations**

All presentations are Quarto Reveal.js presentations. To render:

```bash
# Navigate to directory
cd course_site/day1/presentations

# Render single presentation
quarto render 01_session1_copernicus_philippine_eo.qmd

# Render all presentations
quarto render *.qmd

# Preview in browser
quarto preview 01_session1_copernicus_philippine_eo.qmd
```

### **Viewing Presentations**

After rendering, HTML files are created in `_site/day1/presentations/`. Open them in any modern web browser.

**Presentation Controls:**
- **Arrow keys** or **space** to navigate
- **F** for fullscreen
- **S** for speaker notes view
- **O** for overview mode
- **B** to pause/blackout screen
- **ESC** to exit fullscreen

---

## 📖 For Instructors

### **Before First Use**

1. **Read the Instructor Guide:**
   ```bash
   open INSTRUCTOR_GUIDE.md
   ```
   This contains detailed session-by-session instructions, timing guidance, troubleshooting tips, and teaching best practices.

2. **Test All Presentations:**
   ```bash
   for f in 0*.qmd; do quarto render "$f"; done
   ```
   Ensure all render without errors.

3. **Review Speaker Notes:**
   - Press **S** during presentation to see speaker notes
   - Notes include timing, teaching points, common questions, and transitions

4. **Prepare Jupyter Notebooks:**
   - Session 3 requires: `Day1_Session3_Python_Geospatial_Data.ipynb`
   - Session 4 requires: `Day1_Session4_Google_Earth_Engine.ipynb`
   - Upload to Google Drive and create shareable links

5. **Test Live Demos:**
   - Session 1 includes Copernicus Browser demos
   - Bookmark URLs for quick access during delivery

### **Session Delivery Tips**

**Timing:**
- Each slide with `.timing` class shows time in top-right corner
- Format: `⏱️ 5min | Total: 45min`
- Use these markers to stay on schedule

**Speaker Notes:**
- All slides have comprehensive notes
- Include: timing, key points, transitions, common questions
- Access with **S** key during presentation

**Hands-On Sessions (3 & 4):**
- Share notebook links at session start
- Code together - don't rush ahead
- Pause regularly for questions
- Have teaching assistants monitor chat

---

## 🎨 Presentation Features

### **Styling**

All presentations use `custom.scss` with:
- **Minimal clean design** (per user requirement)
- **Timing indicators** (top-right corner)
- **Readable typography**
- **Simple code highlighting**
- **Professional color scheme**

### **Enhanced Content**

✅ **Timing Structure:** Every session is 2 hours with clear pacing  
✅ **2025 Updates:** Latest satellite launches, AI innovations, Philippine platforms  
✅ **Live Demonstrations:** Integrated with detailed instructor notes  
✅ **Philippine Context:** Local examples, agencies, applications throughout  
✅ **Speaker Notes:** Comprehensive guidance for every slide  
✅ **Break Slides:** 5-minute breaks strategically placed

### **Key 2025 Updates Included**

**Satellite Missions:**
- Sentinel-1C launched December 2024
- Sentinel-2C operational January 2025
- Updated repeat cycles and constellation status

**AI/ML Developments:**
- NASA-IBM Geospatial Foundation Model (Aug 2024)
- ESA Φsat-2 on-board AI (launched 2024)
- Prithvi, Clay foundation models
- Data-centric AI paradigm

**Philippine Infrastructure:**
- PhilSA SIYASAT operational
- DOST P2.6B AI investment (2024-2028)
- SkAI-Pinas 300+ institutions
- PANDA platform details

---

## 🛠️ Technical Requirements

### **For Delivery**

- **Quarto:** >= 1.3
- **Modern Browser:** Chrome/Firefox/Edge (latest)
- **Internet:** Stable connection for live demos
- **Screen Resolution:** 1920x1080 recommended

### **For Participants**

- **Google Account:** For Colab and GEE access
- **Google Earth Engine Account:** Approved before Session 4
- **Modern Browser:** Chrome recommended
- **Internet:** 5+ Mbps download speed

---

## 📋 Session-by-Session Overview

### **Pre-Course Orientation (45-60 min)**
**Format:** Presentation only  
**Focus:** Setup, expectations, logistics  
**Deliverables:** Participants ready with accounts and tools

---

### **Session 1: Copernicus & Philippine EO (120 min)**
**Format:** Presentation with 2 live demos  
**Topics:**
- Copernicus Programme overview
- Sentinel-1 SAR mission
- Sentinel-2 optical mission
- Philippine EO agencies (PhilSA, NAMRIA, DOST-ASTI)
- CoPhil Programme
- Data access methods

**Live Demos:**
1. Sentinel-1 flood monitoring (5 min)
2. Sentinel-2 true color & indices (5 min)

**Deliverables:** Understanding of data sources and Philippine infrastructure

---

### **Session 2: AI/ML Fundamentals (120 min)**
**Format:** Conceptual presentation  
**Topics:**
- AI/ML/DL definitions
- End-to-end ML workflow for EO
- Supervised vs unsupervised learning
- Deep learning & CNNs
- Data-centric AI
- 2025 innovations (foundation models, on-board AI)

**Deliverables:** Conceptual foundation for ML work

---

### **Session 3: Python Geospatial (120 min)**
**Format:** Brief intro + hands-on coding  
**Topics:**
- Google Colab setup
- GeoPandas for vector data (40 min hands-on)
- Rasterio for raster data (50 min hands-on)
- Geospatial operations
- Data preparation for ML

**Required:** Jupyter notebook  
**Deliverables:** Python geospatial coding skills

---

### **Session 4: Google Earth Engine (120 min)**
**Format:** Brief intro + hands-on coding  
**Topics:**
- GEE overview & authentication
- Core concepts (Image, ImageCollection, filtering, reducing)
- Sentinel-1 and Sentinel-2 access
- Cloud masking
- Spectral indices (NDVI, NDWI, NDBI)
- Temporal compositing
- Export workflows

**Required:** Jupyter notebook, GEE account  
**Deliverables:** GEE Python API skills for planetary-scale analysis

---

## 🎯 Learning Outcomes

By the end of Day 1, participants will be able to:

1. ✅ Explain the Copernicus Programme and Sentinel missions
2. ✅ Describe the Philippine EO ecosystem and data infrastructure
3. ✅ Understand AI/ML fundamentals for Earth Observation
4. ✅ Differentiate supervised and unsupervised learning
5. ✅ Recognize data-centric AI principles and 2025 innovations
6. ✅ Load and process vector data with GeoPandas
7. ✅ Read and analyze raster data with Rasterio
8. ✅ Authenticate and use Google Earth Engine Python API
9. ✅ Access and process Sentinel data in GEE
10. ✅ Apply cloud masking, calculate indices, create composites
11. ✅ Export processed data for ML workflows

**Ready for Day 2:** Implementing ML models for real EO applications!

---

## 📁 File Structure

```
course_site/day1/presentations/
│
├── Presentations (Quarto .qmd files)
│   ├── 00_precourse_orientation.qmd
│   ├── 01_session1_copernicus_philippine_eo.qmd
│   ├── 02_session2_ai_ml_fundamentals.qmd
│   ├── 03_session3_python_geospatial.qmd
│   └── 04_session4_google_earth_engine.qmd
│
├── Styling
│   └── custom.scss
│
├── Documentation
│   ├── README.md (this file)
│   ├── INSTRUCTOR_GUIDE.md (detailed teaching guide)
│   ├── IMPLEMENTATION_STATUS.md (development tracker)
│   └── ENHANCEMENT_SUMMARY.md (enhancement framework)
│
└── Rendered Output (after quarto render)
    └── ../../_site/day1/presentations/*.html
```

---

## 🔧 Troubleshooting

### **Presentations Won't Render**

**Error:** "Quarto not found"
```bash
# Install Quarto from https://quarto.org/docs/get-started/
```

**Error:** "custom.scss not found"
```bash
# Ensure custom.scss is in same directory as .qmd files
ls custom.scss
```

**Error:** "Div unclosed warnings"
- These are non-critical warnings
- Presentations still render correctly
- Safe to ignore

### **Live Demos Fail**

**Copernicus Browser slow:**
- Use lower resolution preview
- Have backup screenshots ready
- Pre-load demo areas before session

**Internet connectivity issues:**
- Switch to mobile hotspot
- Share pre-recorded demo videos
- Provide screenshots in chat

### **Hands-On Notebook Issues**

**Colab won't load:**
- Check Google account login
- Clear browser cache
- Try incognito/private window

**Packages fail to install:**
- Restart runtime
- Run installation cell again
- Verify internet connection

**GEE authentication fails:**
- Verify account approved
- Re-run `ee.Authenticate()`
- Check token copied correctly

---

## 📞 Support

**Technical Issues:**
- Google Earth Engine: https://developers.google.com/earth-engine/help
- Quarto: https://github.com/quarto-dev/quarto-cli/discussions
- Colab: https://colab.research.google.com/

**Training Content:**
- CoPhil Programme: https://www.cophil.eu
- PhilSA: https://philsa.gov.ph
- DOST-ASTI: https://asti.dost.gov.ph

---

## 📝 Customization

### **Adding Your Logo**

Edit YAML header in any `.qmd` file:
```yaml
format:
  revealjs:
    logo: images/your-logo.png
```

### **Changing Colors**

Edit `custom.scss`:
```scss
// Section title backgrounds
.reveal section[data-background-color="#1e3a8a"] {
  background-color: #your-color !important;
}
```

### **Adjusting Timing**

Timing markers are data attributes in slide headers:
```markdown
## Slide Title {.timing data-timing="5min" data-cumulative="45min"}
```

Adjust as needed for your delivery pace.

---

## ✅ Quality Checklist

Before delivery, verify:

- [ ] All presentations render without errors
- [ ] Speaker notes display correctly (press S)
- [ ] Timing markers visible on slides
- [ ] Custom CSS loads properly
- [ ] Live demo URLs bookmarked
- [ ] Jupyter notebooks uploaded and shared
- [ ] All participant accounts approved (GEE)
- [ ] Backup internet connection tested
- [ ] Instructor guide reviewed
- [ ] Recording started (if desired)

---

## 🎓 Pedagogical Approach

These presentations follow evidence-based teaching practices:

**Conceptual Before Practical:**
- Theory sessions (1-2) before hands-on (3-4)
- Build mental models first

**Scaffolded Learning:**
- Each session builds on previous
- Day 1 foundation for Days 2-4

**Active Learning:**
- Live demos in Session 1
- Hands-on coding in Sessions 3-4
- Code-along format (not watch-only)

**Contextual Learning:**
- Philippine examples throughout
- Relevant disaster/climate scenarios
- Local agencies and platforms featured

**Formative Assessment:**
- Regular "Questions?" pauses
- Check understanding before moving on
- Troubleshoot errors together

---

## 📚 Additional Resources

**For Further Learning:**
- NASA ARSET: https://appliedsciences.nasa.gov/arset
- EO College: https://eo-college.org
- Google Earth Engine Tutorials: https://developers.google.com/earth-engine/tutorials
- geemap Documentation: https://geemap.org

**Philippine Platforms:**
- PhilSA Space+ Dashboard: (via PhilSA website)
- NAMRIA Geoportal: https://www.geoportal.gov.ph
- DOST-ASTI SkAI-Pinas: https://asti.dost.gov.ph/skai-pinas

---

## 🙏 Acknowledgments

**Developed for:**
CoPhil - EU-Philippines Copernicus Capacity Support Programme

**Based on:**
- Copernicus Programme materials
- Philippine EO ecosystem documentation
- Google Earth Engine tutorials
- Open-source EO/ML resources

**Framework:**
- Quarto for presentation rendering
- Reveal.js for web presentations
- Python ecosystem (GeoPandas, Rasterio, geemap)

---

## 📄 License & Usage

**Training Materials:**
These presentations are developed for the CoPhil Programme. Please respect intellectual property and attribution requirements.

**Code Examples:**
Code snippets in presentations and notebooks are provided for educational use.

**Data Sources:**
- Copernicus Sentinel data: Free and open (terms apply)
- Philippine datasets: Check individual data provider terms
- GEE data catalog: Various licenses per dataset

---

## 🔄 Version History

**Version 1.0 - January 14, 2025**
- Initial complete implementation
- All 6 presentations ready
- Comprehensive instructor guide
- 2025 updates integrated
- Python-only GEE approach
- Tested and production-ready

**Future Updates:**
- Will be versioned and tracked
- Check IMPLEMENTATION_STATUS.md for changes

---

## ✉️ Feedback

**Instructors:** After delivery, please note:
- Timing accuracy (over/under?)
- Sections that worked well
- Confusing parts for participants
- Technical issues encountered
- Suggestions for improvement

This will help refine materials for future deliveries.

---

**Happy Teaching! 🚀**

**For detailed session-by-session guidance, see:** `INSTRUCTOR_GUIDE.md`
