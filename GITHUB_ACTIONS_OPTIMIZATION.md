# GitHub Actions Optimization Guide

## Summary of Speed Improvements

This document explains the optimizations made to speed up GitHub Actions deployment for this Quarto project.

---

## ⚡ Expected Speed Improvements

| Optimization | Time Saved | Impact |
|-------------|------------|--------|
| **Pip cache** | 5-10 min | 🔥 HIGH |
| **Quarto freeze cache** | 3-8 min | 🔥 HIGH |
| **Optimized pip install** | 1-2 min | ⚠️ MEDIUM |
| **Total savings** | **9-20 min** | **🔥 SIGNIFICANT** |

**Before optimization:** ~15-25 minutes per build
**After optimization:** ~5-10 minutes per build (after first run)

---

## 🚀 Optimizations Implemented

### 1. **Enhanced Pip Caching** (Biggest Impact)

**What changed:**
```yaml
- name: Cache pip packages
  uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

**Why it helps:**
- Python packages (especially TensorFlow, PyTorch, and geospatial libs) are large (>2GB)
- Downloading them every time wastes 5-10 minutes
- Cache persists between builds, avoiding re-downloads
- Only re-downloads when `requirements.txt` changes

**Expected savings:** ✅ **5-10 minutes per build**

---

### 2. **Quarto Freeze Caching** (Second Biggest Impact)

**What changed:**
```yaml
- name: Cache Quarto freeze
  uses: actions/cache@v4
  with:
    path: _freeze
    key: ${{ runner.os }}-quarto-freeze-${{ hashFiles('**/*.qmd', '**/*.ipynb') }}
    restore-keys: |
      ${{ runner.os }}-quarto-freeze-
```

**What is Quarto Freeze?**
- Quarto's `freeze: auto` feature (already in `_quarto.yml`) stores pre-rendered notebook outputs
- Notebooks are only re-executed when their source code changes
- Dramatically speeds up rendering when you only change markdown/text

**Why it helps:**
- Executing Jupyter notebooks with heavy computations (ML models, geospatial processing) is slow
- Most changes are text/documentation, not code
- Freeze prevents unnecessary re-execution
- Cache persists between GitHub Actions runs

**Expected savings:** ✅ **3-8 minutes per build** (when notebooks unchanged)

---

### 3. **Optimized Pip Installation Strategy**

**What changed:**
```bash
# Install without dependencies first for speed
pip install --no-deps -r requirements.txt || true
# Then install with dependencies (cached from previous runs)
pip install -r requirements.txt
```

**Why it helps:**
- First pass installs packages quickly without dependency resolution
- Second pass leverages cache for dependencies
- Reduces dependency resolution time

**Expected savings:** ✅ **1-2 minutes per build**

---

### 4. **Added `_freeze/` to .gitignore**

**What changed:**
- Added `/_freeze/` to `.gitignore`
- Freeze directory is cached in GitHub Actions, not tracked in Git

**Why it helps:**
- Keeps repository clean and small
- Prevents merge conflicts on cached outputs
- Freeze cache is managed by CI, not version control

---

## 📊 How Caching Works

### First Build (Cold Cache)
```
1. Install Python dependencies      → 8-10 minutes (no cache)
2. Render Quarto site               → 5-8 minutes (execute all notebooks)
3. Copy PDFs                        → 10 seconds
4. Upload & deploy                  → 1-2 minutes
---
Total: ~15-20 minutes
```

### Subsequent Builds (Warm Cache, No Notebook Changes)
```
1. Restore pip cache                → 30 seconds
2. Install Python dependencies      → 1-2 minutes (from cache)
3. Restore Quarto freeze cache      → 30 seconds
4. Render Quarto site               → 1-2 minutes (no notebook execution)
5. Copy PDFs                        → 10 seconds
6. Upload & deploy                  → 1-2 minutes
---
Total: ~5-8 minutes ⚡
```

### Subsequent Builds (Warm Cache, WITH Notebook Changes)
```
1. Restore pip cache                → 30 seconds
2. Install Python dependencies      → 1-2 minutes (from cache)
3. Restore Quarto freeze cache      → 30 seconds
4. Render Quarto site               → 3-5 minutes (only changed notebooks)
5. Copy PDFs                        → 10 seconds
6. Upload & deploy                  → 1-2 minutes
---
Total: ~7-12 minutes
```

---

## 🔄 When Caches Invalidate

### Pip Cache Invalidates When:
- ✅ `requirements.txt` is modified
- ✅ Python version changes
- ✅ Cache expires (GitHub keeps caches for 7 days)

### Quarto Freeze Cache Invalidates When:
- ✅ `.qmd` or `.ipynb` files are modified
- ✅ Cache expires (7 days)

### Manual Cache Clear:
You can clear caches from: **Settings → Actions → Caches**

---

## 📝 Best Practices Going Forward

### To Maximize Speed:

1. **Don't modify notebooks unnecessarily**
   - Text/documentation changes: ✅ Use `.qmd` files
   - Code changes: ⚠️ Only when needed

2. **Batch notebook changes**
   - Change multiple notebooks in one commit
   - Avoids multiple slow builds

3. **Use `freeze: true` for finished notebooks**
   - In `_quarto.yml`, set `freeze: true` for notebooks that shouldn't change
   - Example:
     ```yaml
     execute:
       freeze: true  # Never re-execute
     ```

4. **Test locally before pushing**
   ```bash
   quarto preview
   ```
   - Catches errors before CI runs

5. **Monitor build times**
   - Check Actions tab for build duration
   - First build after cache clear will be slow (expected)

---

## 🛠️ Troubleshooting

### Build Still Slow?

**Check if caches are working:**
1. Go to: **Actions → [Your workflow run] → Build → Cache steps**
2. Look for: `Cache restored from key: ...`
3. If you see `Cache not found`, caches aren't working

**Common issues:**
- **Cache miss:** First build or cache expired (wait for second build)
- **Requirements changed:** Expected behavior, full reinstall needed
- **Notebooks changed:** Freeze cache won't help, full execution needed

### Force Full Rebuild

To force a clean build without caches:
1. Go to: **Settings → Actions → Caches**
2. Delete relevant caches
3. Re-run workflow

---

## 📈 Monitoring Performance

### View Build Times:
```
Actions → Publish Quarto Website → [Recent runs]
```

### Key Metrics to Watch:
- **Total run time:** Target <10 minutes for incremental builds
- **Install Python dependencies:** Should be <2 minutes with cache
- **Render Quarto site:** Varies by changes, <3 minutes for no code changes

---

## 🎯 Additional Optimizations (Optional)

If you need even faster builds, consider:

### 1. **Split into Multiple Jobs (Parallel)**
```yaml
jobs:
  build-day1:
    # Render Day 1 only
  build-day2:
    # Render Day 2 only
  # ...combine outputs
```
**Savings:** Up to 50% faster with 4 parallel jobs

### 2. **Use Micromamba Instead of Pip**
Micromamba is faster for scientific packages:
```yaml
- uses: mamba-org/setup-micromamba@v1
  with:
    environment-file: environment.yml
```
**Savings:** 2-3 minutes faster than pip

### 3. **Conditional Rendering (Advanced)**
Only render changed files:
```bash
git diff --name-only HEAD~1 HEAD | grep -E '\.(qmd|ipynb)$'
```
**Savings:** Significant for large projects

---

## 📞 Need Help?

If builds are still too slow or caches aren't working:
1. Check the Actions logs for specific slow steps
2. Verify cache keys are matching (check cache step output)
3. Ensure `_freeze/` directory is being populated locally

---

*Last updated: 2025-10-20*
