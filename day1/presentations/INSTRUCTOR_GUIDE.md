# Day 1 Presentations - Instructor Guide

**CoPhil EO AI/ML Training**  
**Last Updated:** January 14, 2025

---

## Overview

This guide provides comprehensive instructions for delivering the five Day 1 presentations. Each session is designed for 2-hour delivery with integrated timing markers, speaker notes, and hands-on exercises.

---

## Pre-Course Preparation

### **Technical Setup (1 Week Before)**

- [ ] Test all presentations render correctly
- [ ] Verify custom.scss loads properly
- [ ] Upload notebooks to Google Drive
- [ ] Create shareable links for notebooks
- [ ] Test GEE authentication process
- [ ] Verify Copernicus Browser access
- [ ] Prepare backup internet connection

### **Participant Setup (3 Days Before)**

Email participants with:

- [ ] Google Earth Engine signup link (approve accounts)
- [ ] Google Colab access verification
- [ ] Zoom/meeting platform test
- [ ] Course materials access links
- [ ] Pre-course orientation slide deck

### **Day-Of Setup (Morning)**

- [ ] Load all presentations
- [ ] Test screen sharing
- [ ] Share notebook links in chat
- [ ] Have backup slides ready
- [ ] Start recording (if applicable)

---

## Session-by-Session Guide

---

## **Pre-Course Orientation** (45-60 minutes)

**File:** `00_precourse_orientation.qmd`  
**When:** Before Day 1 or early morning Day 1  
**Format:** Presentation only

### Key Sections

1. **Welcome & Introductions (10 min)**
   - Instructor introductions
   - Participant introductions (if small group)
   - Icebreaker activity

2. **Technical Setup (15 min)**
   - Google Earth Engine account verification
   - Colab access test
   - Zoom features walkthrough

3. **Course Overview (15 min)**
   - 4-day structure
   - Daily topics
   - Expected outcomes

4. **Logistics & Expectations (10 min)**
   - Schedule (breaks, lunch)
   - Code of conduct
   - How to ask questions
   - Recording/screenshot policies

### Instructor Tips

- **Go slow** - participants may be anxious about technology
- **Do live checks** - "Raise hand if GEE approved"
- **Set expectations** - coding errors are normal and expected
- **Build rapport** - create supportive learning environment

---

## **Session 1: Copernicus & Philippine EO** (120 minutes)

**File:** `01_session1_copernicus_philippine_eo.qmd`  
**Format:** Presentation with live demos  
**Slides:** ~70 slides

### Timing Breakdown

| Section | Time | Cumulative |
|---------|------|------------|
| Introduction & Roadmap | 12 min | 12 min |
| Copernicus Overview | 7 min | 19 min |
| Sentinel-1 SAR | 30 min | 50 min |
| **Live Demo: Sentinel-1** | 5 min | 55 min |
| Sentinel-2 Optical | 10 min | 65 min |
| **Live Demo: Sentinel-2** | 5 min | 70 min |
| **☕ Break** | 5 min | 75 min |
| Philippine EO Landscape | 3 min | 78 min |
| PhilSA & SIYASAT | 8 min | 86 min |
| NAMRIA | 4 min | 90 min |
| DOST-ASTI & SkAI-Pinas | 6 min | 96 min |
| CoPhil Programme | 10 min | 106 min |
| Data Access Methods | 12 min | 118 min |
| Summary & Q&A | 3 min | 121 min |

### Key Teaching Points

**Sentinel-1 (SAR):**
- All-weather, day-night capability
- VV polarization for water detection
- Sentinel-1C launched December 2024 (NEW!)
- 6-day repeat cycle with constellation

**Sentinel-2 (Optical):**
- 13 spectral bands, 10m resolution
- Sentinel-2C operational January 2025 (NEW!)
- 5-day repeat cycle
- L2A = analysis-ready (atmospherically corrected)

**Philippine Context:**
- PhilSA: National space agency, CoPhil co-chair
- SIYASAT: Operational NovaSAR-1 data portal
- DOST P2.6B AI investment (2024-2028)
- SkAI-Pinas: 300+ institutions supported

### Live Demo Instructions

**Demo 1: Sentinel-1 Flood Monitoring (5 min)**

1. Open Copernicus Browser: https://dataspace.copernicus.eu
2. Navigate to Philippines (recent typhoon area if available)
3. Select Sentinel-1 GRD IW
4. Choose date before typhoon
5. Add comparison date after typhoon
6. Show VV band - dark areas = water
7. Use time slider for animation
8. Explain bright (urban/rough) vs dark (water/smooth)

**Common Questions:**
- Q: "Why grainy?" A: Speckle is inherent to SAR
- Q: "Can we download?" A: Yes, covered in Session 4

**Demo 2: Sentinel-2 True Color & Indices (5 min)**

1. Navigate to Palawan or Metro Manila
2. Select Sentinel-2 L2A
3. Filter cloud cover <20%
4. Show True Color RGB (B4-B3-B2)
5. Switch to False Color (B8-B4-B3) - vegetation = RED
6. Show SWIR composite (B12-B8-B4)
7. Calculate NDVI: (B8-B4)/(B8+B4)
8. Use time slider to show change

**Common Questions:**
- Q: "Which bands?" A: Depends on application (Day 2 topic)
- Q: "Clouds?" A: Use cloud masks (Session 4)

### Troubleshooting

- **Browser slow?** Use lower resolution preview
- **Can't find area?** Use search box or coordinates
- **Demo fails?** Have backup screenshots ready

### Transition to Session 2

"We've covered WHERE data comes from and WHAT satellites collect. Next: HOW to use AI/ML to extract information from this data."

---

## **Session 2: AI/ML Fundamentals** (120 minutes)

**File:** `02_session2_ai_ml_fundamentals.qmd`  
**Format:** Conceptual presentation  
**Slides:** ~80 slides

### Timing Breakdown

| Section | Time | Cumulative |
|---------|------|------------|
| Objectives & Roadmap | 4 min | 4 min |
| What is AI/ML? | 6 min | 10 min |
| EO ML Workflow | 25 min | 35 min |
| Supervised Learning | 25 min | 60 min |
| **☕ Break** | 5 min | 65 min |
| Unsupervised Learning | 5 min | 70 min |
| Deep Learning & CNNs | 20 min | 90 min |
| Data-Centric AI | 7 min | 97 min |
| **2025 Innovations** | 10 min | 107 min |
| Summary & Q&A | 13 min | 120 min |

### Key Teaching Points

**Foundational Concepts:**
- AI > ML > DL (nested relationship)
- ML learns from data, not hard-coded rules
- EO workflow: Problem → Data → Preprocessing → Features → Model → Validation → Deployment

**Supervised vs Unsupervised:**
- Supervised: Labeled data (classification, regression)
- Unsupervised: No labels (clustering, anomaly detection)
- Most EO applications use supervised learning

**Deep Learning:**
- Neural networks with many layers
- CNNs excel at image analysis
- Data-hungry (1000s of samples)
- GPU required for training

**2025 Updates (CRITICAL):**
- **Foundation Models:** NASA-IBM, Prithvi, Clay
- **Key benefit:** 100s of samples vs 1000s needed
- **On-board AI:** ESA Φsat-2 (2024), Satellogic
- **Philippine relevance:** Reduce labeling burden

### Teaching Strategy

**This session is CONCEPTUAL.** Focus on:
- Building intuition, not math
- Real EO examples throughout
- Philippine disaster response scenarios
- Setting up mental models for hands-on Days 2-4

### Common Questions & Answers

**Q:** "Do I need a GPU?"  
**A:** Not for Random Forest (Day 2). Yes for deep learning (Day 3).

**Q:** "How many labeled samples?"  
**A:** Depends:
- Random Forest: 100-500 per class
- CNN from scratch: 1000s per class
- Foundation model fine-tuning: 100-200 per class

**Q:** "Which algorithm should I use?"  
**A:** Start simple (Random Forest), move to DL if needed and you have data/compute.

**Q:** "Can we use foundation models for Philippines?"  
**A:** YES! They're global and open-source. Perfect for low-resource scenarios.

### Transition to Session 3

"Now you understand ML concepts. Next: Learn the Python tools to actually implement these workflows."

---

## **Session 3: Python Geospatial** (120 minutes)

**File:** `03_session3_python_geospatial.qmd`  
**Format:** Brief intro + HANDS-ON coding  
**Slides:** ~30 slides + Jupyter notebook

### Timing Breakdown

| Section | Time | Cumulative |
|---------|------|------------|
| Objectives & Roadmap | 7 min | 7 min |
| Python Basics Recap | 8 min | 15 min |
| **GeoPandas HANDS-ON** | 40 min | 55 min |
| **☕ Break** | 5 min | 60 min |
| **Rasterio HANDS-ON** | 50 min | 110 min |
| Summary & Q&A | 10 min | 120 min |

### Jupyter Notebook

**File:** `Day1_Session3_Python_Geospatial_Data.ipynb`

**Critical:** Share link at start of session!

### Session Flow

**1. Introduction (7 min)**
- Learning objectives
- Roadmap
- Notebook access instructions

**2. Setup (5 min)**
- Participants open notebook
- Save copy to Drive
- Run installation cell
- Verify packages load

**3. GeoPandas Section (40 min)**

**Instructor demonstrates, participants follow:**

- Load Philippine boundaries shapefile
- Explore GeoDataFrame (`.head()`, `.crs`, `.plot()`)
- Filter by region
- Reproject to UTM
- Calculate area
- Spatial join with points
- Export to GeoJSON

**Pacing:**
- Demonstrate each cell
- Wait for participants to run
- Check for errors in chat
- Pause every 5-10 minutes for questions

**4. Break (5 min)**

**5. Rasterio Section (50 min)**

**Instructor demonstrates, participants follow:**

- Read Sentinel-2 GeoTIFF
- Examine metadata (`.meta`, `.crs`, `.bounds`)
- Read specific bands
- Visualize with matplotlib
- Calculate NDVI
- Mask by vector boundary
- Crop raster
- Export processed raster

**Common Errors & Solutions:**

| Error | Solution |
|-------|----------|
| ModuleNotFoundError | Restart runtime, reinstall |
| FileNotFoundError | Check file path, mount Drive |
| CRS mismatch warning | Reproject before operations |
| MemoryError | Use windowed reading |
| NoData not handled | Use `.masked_array` |

### Troubleshooting Protocol

**Level 1: Self-Help**
- Check previous cells ran successfully
- Verify variable names match
- Look for typos

**Level 2: Peer Help**
- Encourage participants to help each other in breakout rooms

**Level 3: TA/Instructor**
- Teaching assistant monitors chat
- Screen share for debugging
- Create breakout room if needed

### Instructor Tips

- **Code together** - don't rush ahead
- **Explain output** - what does each cell produce?
- **Live debugging** - when errors occur, debug together
- **Encourage exploration** - "Try changing the band numbers"
- **No shame in errors** - normalize mistakes

### Transition to Session 4

"You can now work with geospatial data in Python. Next: Scale up to planetary analysis with Google Earth Engine."

---

## **Session 4: Google Earth Engine** (120 minutes)

**File:** `04_session4_google_earth_engine.qmd`  
**Format:** Brief intro + HANDS-ON coding (Python only)  
**Slides:** ~60 slides + Jupyter notebook

### Timing Breakdown

| Section | Time | Cumulative |
|---------|------|------------|
| GEE Overview | 7 min | 7 min |
| Authentication | 8 min | 15 min |
| Core Concepts | 18 min | 33 min |
| **Sentinel Access HANDS-ON** | 15 min | 48 min |
| **☕ Break** | 5 min | 60 min |
| **Cloud Masking HANDS-ON** | 10 min | 70 min |
| **Indices & Composites HANDS-ON** | 20 min | 90 min |
| **Time Series HANDS-ON** | 11 min | 101 min |
| Export Workflows | 9 min | 110 min |
| Summary & Q&A | 10 min | 120 min |

### Critical Pre-Session Check

**⚠️ IMPORTANT:** Verify all participants have GEE accounts approved!

- Email reminder 3 days before
- Check status at session start
- Have fallback plan for unapproved accounts

### Jupyter Notebook

**File:** `Day1_Session4_Google_Earth_Engine.ipynb`

### Authentication Process (CRITICAL)

**First Time Setup (8 min):**

```python
import ee
import geemap

# Authenticate (opens browser)
ee.Authenticate()

# Initialize
ee.Initialize()
```

**Steps:**
1. Run `ee.Authenticate()`
2. Browser tab opens
3. Sign in with Google account
4. Allow Earth Engine access
5. Copy verification code
6. Paste back in notebook
7. Run `ee.Initialize()`

**Troubleshooting:**
- "Not approved" → Account pending, follow along for now
- "Token invalid" → Re-authenticate
- "Module not found" → `pip install geemap`

### Live Coding Exercises

**Exercise 1: Load Sentinel-2 (5 min)**
```python
s2 = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
```
- Explain collection ID
- Show filtering (spatial, temporal, cloud)
- Print collection size

**Exercise 2: Visualize True Color (5 min)**
```python
Map = geemap.Map()
Map.addLayer(image, vis_params, 'S2 RGB')
```
- Create interactive map
- Add layer with visualization parameters
- Explore (zoom, pan, inspect)

**Exercise 3: False Color (5 min)**
- Change band combination to NIR-R-G
- Vegetation appears red
- Discuss band combinations

**Exercise 4: Sentinel-1 SAR (5 min)**
- Load S1 GRD collection
- Filter by polarization (VV)
- Visualize median composite
- Dark = water, Bright = urban

**BREAK (5 min)**

**Exercise 5: Cloud Masking (10 min)**
- Define cloud mask function using QA60
- Apply to collection with `.map()`
- Create median composite
- Compare masked vs unmasked

**Exercise 6: NDVI Calculation (5 min)**
- Use `.normalizedDifference(['B8', 'B4'])`
- Visualize with green palette
- Interpret values

**Exercise 7: Other Indices (5 min)**
- NDWI for water
- NDBI for built-up areas
- Add multiple layers to map

**Exercise 8: Temporal Compositing (10 min)**
- Filter by seasons (dry vs wet)
- Calculate NDVI for both
- Compute change
- Visualize difference

**Exercise 9: Time Series (11 min)**
- Define point of interest
- Extract NDVI time series
- Convert to pandas DataFrame
- Plot with matplotlib

**Exercise 10: Export (9 min)**
- Export image to Google Drive
- Check task status
- Discuss export parameters

### Key Concepts to Emphasize

**Server-Side vs Client-Side:**
- Most computation on Google servers (fast)
- Only download final results (small)
- Never download petabytes!

**Filtering Best Practices:**
- Filter spatial first (most efficient)
- Then temporal
- Then property (cloud cover)

**Reducers:**
- `.median()` for cloud-free composites
- `.mean()` for average conditions
- `.min()` / `.max()` for extremes

**Python vs JavaScript:**
- Same concepts, different syntax
- Python better for ML integration
- JavaScript better for quick prototyping

### Common Issues

| Issue | Solution |
|-------|----------|
| "Computation timeout" | Reduce area or resolution |
| "User memory exceeded" | Use `.limit()` or sample |
| "No features in collection" | Check filters (too restrictive?) |
| "Tile error" | Refresh map |
| "Export fails" | Check maxPixels, region size |

### Philippine Example Deep Dive

**Rice Monitoring Workflow (10 min):**

1. Define rice-growing region (Central Luzon)
2. Load one year of Sentinel-2
3. Apply cloud masking
4. Create monthly composites
5. Calculate NDVI for each month
6. Visualize seasonal pattern
7. Export time series

**Teaching points:**
- This workflow applies to ANY EO application
- Pattern: AOI → Filter → Mask → Composite → Calculate → Visualize → Export
- Students will use this pattern all week

### Transition to Day 2

"You now have all the tools: Data access (GEE), Processing (Python), Concepts (ML). Tomorrow: Build actual ML models for real problems!"

---

## General Teaching Best Practices

### Timing Management

- **Use timing markers** - displayed on every slide
- **Set timer on phone** - stay on track
- **Build in buffer** - 5-10 min extra per session
- **Skip if needed** - mark optional slides
- **Never skip breaks** - participant attention suffers

### Participant Engagement

**Questions:**
- Pause regularly: "Questions so far?"
- Normalize questions: "Great question!"
- Defer if needed: "Let's cover that in Session X"
- Answer in chat if off-topic

**Hands-On Sessions:**
- **Code together** - don't rush ahead
- **Screen share** - show your notebook
- **Wait for slowest** - check progress regularly
- **Celebrate success** - "Nice work everyone!"

**Interactivity:**
- Polls: "Have you used GEE before?"
- Chat responses: "Type your primary application area"
- Show of hands: "Who got the same result?"

### Accessibility

- **Speak clearly** - pace yourself
- **Describe visuals** - don't assume everyone can see
- **Provide transcripts** - for recordings
- **Multiple formats** - slides + notebooks + documentation
- **Record sessions** - for review

### Error Handling

**When something breaks:**
1. **Stay calm** - model debugging mindset
2. **Explain error** - teach what it means
3. **Debug together** - walk through solution
4. **Have backup** - screenshots of expected output
5. **Move on** - don't spend 10 min on one person's issue

**Common Fixes:**
- Restart kernel/runtime
- Clear output and re-run
- Check previous cells executed
- Verify file paths
- Check internet connection

### Cultural Sensitivity

**Philippine Context:**
- Use local examples (typhoons, provinces, crops)
- Respect naming conventions (e.g., use "Philippines" not "PI")
- Acknowledge local expertise (participants may know regions better)
- Highlight Philippine agencies (PhilSA, NAMRIA, DOST-ASTI)

### Energy Management

**Instructor Self-Care:**
- Hydrate during breaks
- Stand during presentations (energy)
- Sit during hands-on (less tiring)
- Tag-team with co-instructor if possible

**Participant Energy:**
- Morning: High energy, conceptual content
- Pre-lunch: Hands-on (engagement)
- Post-lunch: Lighter content, more interaction
- Late afternoon: Hands-on, peer learning

---

## Day 1 Schedule Summary

| Time | Session | Format |
|------|---------|--------|
| 08:00-09:00 | Pre-Course Orientation | Presentation |
| 09:00-11:00 | Session 1: Copernicus & PH EO | Presentation + Demos |
| 11:00-11:15 | **Break** | - |
| 11:15-13:15 | Session 2: AI/ML Fundamentals | Presentation |
| 13:15-14:15 | **Lunch** | - |
| 14:15-16:15 | Session 3: Python Geospatial | Hands-On |
| 16:15-16:30 | **Break** | - |
| 16:30-18:30 | Session 4: Google Earth Engine | Hands-On |
| **Total** | **~8 hours** | **(excluding breaks/lunch)** |

---

## Technical Requirements Checklist

### For Instructors

- [ ] Laptop with HDMI output
- [ ] Backup laptop
- [ ] Reliable internet (wired preferred)
- [ ] Mobile hotspot backup
- [ ] Presentation remote/clicker
- [ ] Second monitor (helpful)
- [ ] Google account with GEE access
- [ ] All notebooks tested and working

### For Participants

- [ ] Laptop (Windows/Mac/Linux)
- [ ] Modern web browser (Chrome recommended)
- [ ] Internet connection (5+ Mbps)
- [ ] Google account
- [ ] GEE account (approved)
- [ ] Zoom client installed
- [ ] Microphone and camera (optional but encouraged)

### Platform Access

- [ ] Zoom/meeting room tested
- [ ] Screen sharing permissions
- [ ] Recording enabled (if desired)
- [ ] Breakout rooms configured
- [ ] Waiting room settings
- [ ] Chat enabled
- [ ] Polls prepared (if using)

---

## Backup Plans

### Internet Failure

**Instructor:**
- Switch to mobile hotspot
- Use backup internet connection
- Have offline copy of slides
- Share pre-recorded demo videos

**Participant:**
- Provided recorded sessions for later review
- Share download links for offline notebooks
- Email homework assignments

### GEE Authentication Issues

- Follow along with instructor screen
- Work on authentication during break/after session
- Provide authenticated notebook outputs as reference
- Revisit in Day 2 morning if needed

### Notebook Failures

- Share Google Drive backup copies
- Provide Binder/Colab alternative links
- Have downloadable .ipynb files
- Screen share instructor notebook as fallback

---

## Post-Session Actions

### After Each Session

- [ ] Save chat log (questions, links)
- [ ] Note timing (over/under?)
- [ ] Identify confusing sections
- [ ] List common errors encountered
- [ ] Send follow-up email with resources

### End of Day 1

- [ ] Send Day 2 preview
- [ ] Share all notebook links again
- [ ] Provide optional homework (review exercises)
- [ ] Remind about Day 2 start time
- [ ] Ask for feedback (short survey)

---

## Instructor Tips by Session

### Session 1: Keep Energy High
- This sets the tone for entire week
- Show enthusiasm for Copernicus data
- Make demos engaging (zoom, pan, compare)
- Connect to Philippine examples

### Session 2: Build Intuition
- Don't get lost in math
- Use analogies and metaphors
- Draw diagrams on whiteboard/annotate slides
- Emphasize "why" over "what"

### Session 3: Patient Debugging
- First hands-on session - expect hiccups
- Slow down for errors
- Model good debugging practices
- Celebrate small wins

### Session 4: Pull It All Together
- Show how GEE connects to previous sessions
- Reference Session 1 (data), Session 2 (ML), Session 3 (Python)
- Preview Day 2 (using GEE for ML training data)
- End on high note (exciting preview)

---

## Emergency Contacts & Resources

**Technical Support:**
- Google Earth Engine Support: https://developers.google.com/earth-engine/help
- Colab Help: https://colab.research.google.com/
- geemap Issues: https://github.com/giswqs/geemap/issues

**Content Resources:**
- CoPhil Programme: https://www.cophil.eu
- Copernicus Data Space: https://dataspace.copernicus.eu
- PhilSA: https://philsa.gov.ph

**Instructor Notes:**
- Keep this guide handy during delivery
- Mark your own notes in margins
- Update after each delivery (lessons learned)
- Share improvements with co-instructors

---

## Success Metrics

**By end of Day 1, participants should be able to:**

✅ Explain what Copernicus provides and why it's valuable  
✅ Describe Philippine EO infrastructure  
✅ Differentiate supervised vs unsupervised ML  
✅ Understand data-centric AI principles  
✅ Load and visualize geospatial data in Python  
✅ Authenticate and use Google Earth Engine  
✅ Access and process Sentinel data in GEE  
✅ Feel confident for Day 2 ML implementation

**Indicators of Success:**
- Questions in chat (engagement)
- Code running successfully (technical proficiency)
- Positive feedback (satisfaction)
- Enthusiasm for Day 2 (motivation)

---

## Final Reminders

🎯 **Be flexible** - adapt to participant needs  
🎯 **Be encouraging** - celebrate progress  
🎯 **Be patient** - learning takes time  
🎯 **Be enthusiastic** - your energy is contagious  
🎯 **Be prepared** - test everything beforehand

**Good luck and enjoy the training! 🚀**
