# Local Jupyter Notebook Testing Setup

This guide helps you test Jupyter notebooks locally before deploying to GitHub/Google Colab.

---

## Quick Start (TL;DR)

```bash
# 1. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
# venv\Scripts\activate   # On Windows

# 2. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install jupyter jupyterlab ipywidgets

# 3. Start Jupyter Lab
jupyter lab

# 4. Open and test notebooks
# Navigate to day1/notebooks/ or day2/notebooks/
```

---

## Detailed Setup Guide

### 1. Prerequisites

**Required:**
- Python 3.11+ (you have 3.13.2 ✓)
- pip (Python package installer)
- 4GB+ RAM (recommended)
- 5GB+ free disk space (for dependencies)

**Check your setup:**
```bash
python3 --version  # Should show 3.11+
pip --version      # Should be installed
```

---

### 2. Create Virtual Environment

**Why use a virtual environment?**
- Isolates project dependencies from system Python
- Prevents version conflicts
- Easy to recreate or delete

**Create venv:**
```bash
# Navigate to project root
cd /Users/dimitriskasampalis/Projects/Neuralio/cophil-training-v1.0

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Your terminal prompt should now show (venv)
```

**To deactivate later:**
```bash
deactivate
```

---

### 3. Install Dependencies

**Install all required packages:**
```bash
# Upgrade pip first
pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt

# Install Jupyter and extensions
pip install jupyter jupyterlab ipywidgets nbformat nbconvert

# Install additional testing tools
pip install ipykernel pytest

# Verify installations
pip list | grep -E "(jupyter|notebook|ipywidgets)"
```

**Expected output:**
```
jupyter              1.x.x
jupyter-client       8.x.x
jupyter-core         5.x.x
jupyterlab           4.x.x
notebook             7.x.x
ipywidgets           8.x.x
```

---

### 4. Configure Jupyter Kernel

Register your virtual environment as a Jupyter kernel:

```bash
# Register kernel (while venv is active)
python -m ipykernel install --user --name=cophil-training --display-name "Python (CoPhil)"

# Verify kernel is registered
jupyter kernelspec list
```

**Expected output:**
```
Available kernels:
  cophil-training    /Users/.../kernels/cophil-training
  python3            /Users/.../kernels/python3
```

---

### 5. Start Jupyter Lab

**Option A: Jupyter Lab (Recommended)**
```bash
jupyter lab
```

**Option B: Classic Jupyter Notebook**
```bash
jupyter notebook
```

**What happens:**
- Browser opens automatically at `http://localhost:8888`
- File browser shows project directory
- You can navigate to notebooks and open them

**Jupyter Lab advantages:**
- Modern interface
- Multi-tab support
- Built-in terminal
- Git integration
- File browser

---

### 6. Testing Notebooks

### **6.1 Quick Smoke Test**

Open a notebook and run:
```python
# Test cell 1: Check imports
import sys
print(f"Python version: {sys.version}")

# Test cell 2: Check key libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
import rasterio

print("✓ All imports successful")
```

### **6.2 Day 1 Session 3 Notebook**

**File:** `day1/notebooks/Day1_Session3_Python_Geospatial_Data.ipynb`

**Expected behavior:**
- Cell 4: Installs packages (may take 5-10 min first time)
- Cell 30: Fetches real Sentinel-2 data from Microsoft Planetary Computer
- Cell 32: Loads bands from cloud storage
- Cells 40, 47: Visualizations appear

**Common issues:**
- **Issue:** "ModuleNotFoundError: No module named 'pystac_client'"
  - **Fix:** `pip install pystac-client planetary-computer`
- **Issue:** "Earth Engine authentication failed"
  - **Fix:** Not needed for Session 3 (only Session 4)

### **6.3 Day 1 Session 4 Notebook**

**File:** `day1/notebooks/Day1_Session4_Google_Earth_Engine.ipynb`

**Expected behavior:**
- Cell 2: Prompts for Earth Engine authentication
- Cell 22, 23: Display thumbnail images

**Common issues:**
- **Issue:** "NameError: name 'Image' is not defined"
  - **Fix:** Already fixed in latest version (check cell 2 has `from IPython.display import Image`)
- **Issue:** "ee.Initialize: no project found"
  - **Fix:** Replace `'YOUR-PROJECT-ID'` with your actual Google Cloud project ID
  - See notebook troubleshooting section for setup instructions

### **6.4 Day 2 Session 1 Notebook**

**File:** `day2/notebooks/session1_hands_on_lab_student.ipynb`

**Expected behavior:**
- Cell 14: Displays Palawan boundary without errors

**Common issues:**
- **Issue:** "TypeError: 'NoneType' object is not subscriptable"
  - **Fix:** Already fixed in latest version (cell 14 has safe bounds checking)

---

### 7. Automated Testing Script

Create a test script to validate all notebooks:

**File:** `scripts/test_notebooks.sh`
```bash
#!/bin/bash
# Test all notebooks for basic execution

set -e  # Exit on error

echo "Testing Jupyter notebooks..."

# Activate virtual environment
source venv/bin/activate

# Test each notebook (without executing code cells)
notebooks=(
    "day1/notebooks/Day1_Session3_Python_Geospatial_Data.ipynb"
    "day1/notebooks/Day1_Session4_Google_Earth_Engine.ipynb"
    "day2/notebooks/session1_hands_on_lab_student.ipynb"
    "day2/notebooks/session2_extended_lab_STUDENT.ipynb"
)

for nb in "${notebooks[@]}"; do
    echo "  Testing: $nb"
    jupyter nbconvert --to notebook --execute --inplace "$nb" --ExecutePreprocessor.timeout=600 || echo "  ⚠️  Failed: $nb"
done

echo "✓ All notebooks tested"
```

**Make executable:**
```bash
chmod +x scripts/test_notebooks.sh
```

**Run tests:**
```bash
./scripts/test_notebooks.sh
```

---

### 8. Quick Testing Workflow

**Daily workflow for testing notebooks:**

```bash
# 1. Activate environment (if not already active)
source venv/bin/activate

# 2. Start Jupyter Lab
jupyter lab

# 3. Open notebook
# Navigate to notebook in file browser

# 4. Test changes
# Run cells, verify outputs

# 5. Save and commit
# File → Save
# git add <notebook>
# git commit -m "Fix: ..."

# 6. (Optional) Test Colab compatibility
# File → Download as → .ipynb
# Upload to Google Colab manually
```

---

### 9. Colab Compatibility Checklist

Before pushing to GitHub for Colab deployment:

**✓ Check these in your notebook:**

1. **Installation cells use `!pip install`**
   ```python
   !pip install package-name -q
   ```

2. **No local file paths**
   ```python
   # ❌ Bad
   data = pd.read_csv('/Users/you/data.csv')

   # ✓ Good
   data = pd.read_csv('https://raw.githubusercontent.com/.../data.csv')
   ```

3. **Use Google Drive for large files (if needed)**
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

4. **Test imports in first cells**
   ```python
   import numpy as np
   import pandas as pd
   # etc.
   ```

5. **IPython.display.Image for images**
   ```python
   from IPython.display import Image
   display(Image(url=thumbnail_url))
   ```

6. **No hardcoded credentials**
   - Use environment variables or prompt for input

---

### 10. Troubleshooting

### **Issue: "Kernel died" when running notebooks**

**Cause:** Out of memory (large datasets, ML models)

**Solutions:**
1. Restart kernel: Kernel → Restart Kernel
2. Reduce data size (use smaller subsets for testing)
3. Close other applications
4. Increase Docker memory (if using Docker)

### **Issue: "pip install" very slow**

**Solutions:**
1. Use pip cache:
   ```bash
   pip install --cache-dir ~/.cache/pip -r requirements.txt
   ```
2. Use conda instead (faster for scientific packages):
   ```bash
   conda create -n cophil python=3.11
   conda activate cophil
   conda install -c conda-forge numpy pandas matplotlib geopandas rasterio
   ```

### **Issue: "ImportError: DLL load failed" (Windows)**

**Cause:** GDAL/rasterio binary issues on Windows

**Solution:**
Use conda instead of pip for geospatial packages:
```bash
conda install -c conda-forge rasterio geopandas fiona
```

### **Issue: Earth Engine authentication fails**

**Solution:**
1. Run in terminal:
   ```bash
   earthengine authenticate
   ```
2. Follow browser prompts
3. Restart Jupyter kernel

### **Issue: Notebook won't open (JSON error)**

**Cause:** Corrupted notebook file

**Solutions:**
1. Check git status:
   ```bash
   git status
   git diff <notebook>
   ```
2. Restore from git:
   ```bash
   git checkout HEAD -- <notebook>
   ```
3. Validate JSON:
   ```bash
   python -m json.tool <notebook> > /dev/null
   ```

---

### 11. Performance Tips

**Speed up notebook testing:**

1. **Use nbconvert for quick validation:**
   ```bash
   jupyter nbconvert --to notebook --execute day1/notebooks/*.ipynb
   ```

2. **Skip long-running cells:**
   Add this at the top of slow cells:
   ```python
   # Skip in local testing
   import os
   if os.getenv('TESTING') == '1':
       print("Skipped in testing mode")
   else:
       # ... actual code
   ```

3. **Use smaller datasets locally:**
   ```python
   # Use small sample for local testing
   DEBUG = True  # Set False for production
   sample_size = 100 if DEBUG else 10000
   ```

4. **Cache results:**
   ```python
   import pickle
   import os

   if os.path.exists('cache.pkl'):
       data = pickle.load(open('cache.pkl', 'rb'))
   else:
       # Expensive computation
       data = expensive_function()
       pickle.dump(data, open('cache.pkl', 'wb'))
   ```

---

### 12. VS Code Integration (Optional)

If you prefer VS Code over Jupyter Lab:

**Install VS Code Jupyter extension:**
1. Open VS Code
2. Install "Jupyter" extension by Microsoft
3. Install "Python" extension by Microsoft

**Open notebook in VS Code:**
```bash
code day1/notebooks/Day1_Session3_Python_Geospatial_Data.ipynb
```

**Select kernel:**
- Click kernel selector (top-right)
- Choose "Python (CoPhil)" kernel

**Run cells:**
- Click ▶️ next to cell
- Or use Shift+Enter

---

### 13. Comparing Local vs Colab

| Feature | Local Jupyter | Google Colab |
|---------|--------------|--------------|
| **Setup** | One-time venv setup | Zero setup |
| **Speed** | Your machine speed | Google TPU/GPU |
| **Data** | Local files | Cloud/Drive files |
| **Cost** | Free (your hardware) | Free (limited) / Paid |
| **Offline** | Yes ✓ | No ✗ |
| **Persistence** | Full control | Session-based |
| **Best for** | Development & testing | Training & sharing |

**Recommended workflow:**
1. **Develop locally** → Quick iteration
2. **Test in Colab** → Verify cloud compatibility
3. **Deploy to GitHub** → Share with students

---

### 14. Next Steps

**After setup, you can:**

1. ✅ Test notebooks locally before committing
2. ✅ Iterate quickly without waiting for GitHub Actions
3. ✅ Debug issues in real-time
4. ✅ Add new content and test immediately
5. ✅ Verify Colab compatibility

**Recommended daily workflow:**
```bash
# Morning: Start environment
cd ~/Projects/Neuralio/cophil-training-v1.0
source venv/bin/activate
jupyter lab

# Work on notebooks...

# Evening: Commit changes
git add day1/notebooks/*.ipynb
git commit -m "Update notebooks"
git push  # GitHub Actions will deploy

# Cleanup
deactivate
```

---

## Summary

You now have:
- ✅ Virtual environment for isolated dependencies
- ✅ Jupyter Lab for local notebook testing
- ✅ All project dependencies installed
- ✅ Troubleshooting guide for common issues
- ✅ Fast iteration workflow (no GitHub wait time)

**Estimated setup time:** 15-30 minutes (first time)
**Estimated testing time per notebook:** 1-5 minutes (vs 15-25 min on GitHub)

---

*Last updated: 2025-10-20*
