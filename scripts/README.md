# CoPhil Training Scripts

Helper scripts for local development and testing.

---

## Quick Start

### First-time Setup

```bash
# Run setup script (one time only)
./scripts/setup_local_env.sh

# This will:
# - Create virtual environment
# - Install all dependencies
# - Configure Jupyter Lab
# - Register Jupyter kernel
```

**Time:** ~10-15 minutes

---

## Daily Use

### Start Jupyter Lab

```bash
./scripts/start_jupyter.sh
```

This automatically:
- Activates virtual environment
- Starts Jupyter Lab
- Opens browser

### Test Notebooks

```bash
# Test all notebooks
./scripts/test_notebooks.sh

# Test specific notebook
./scripts/test_notebooks.sh day1/notebooks/Day1_Session3_Python_Geospatial_Data.ipynb
```

This validates:
- JSON structure
- Syntax errors
- Basic integrity

---

## Available Scripts

### `setup_local_env.sh`

**Purpose:** One-time environment setup

**Usage:**
```bash
./scripts/setup_local_env.sh
```

**What it does:**
1. Checks Python version (3.11+ recommended)
2. Creates virtual environment (`venv/`)
3. Installs all requirements from `requirements.txt`
4. Installs Jupyter Lab and extensions
5. Registers Jupyter kernel
6. Verifies all installations

**When to run:**
- First time setting up project
- After cloning repository
- After major dependency updates
- If venv gets corrupted

---

### `start_jupyter.sh`

**Purpose:** Quick start Jupyter Lab

**Usage:**
```bash
./scripts/start_jupyter.sh
```

**What it does:**
1. Activates virtual environment
2. Checks Jupyter is installed
3. Starts Jupyter Lab
4. Opens browser automatically

**Shortcuts:**
- Stop: Press `Ctrl+C` in terminal
- Access: http://localhost:8888

---

### `test_notebooks.sh`

**Purpose:** Validate notebooks before committing

**Usage:**
```bash
# Test all notebooks
./scripts/test_notebooks.sh

# Test specific notebook
./scripts/test_notebooks.sh path/to/notebook.ipynb

# Test with execution (slow)
./scripts/test_notebooks.sh --execute
```

**What it tests:**
- ✅ JSON structure valid
- ✅ No syntax errors
- ✅ Can be converted
- ⊘ Cell execution (optional, slow)

**When to run:**
- Before committing notebook changes
- After major edits
- Before pushing to GitHub
- As part of pre-commit hook

---

## Manual Commands

If you prefer manual control:

### Activate Environment

```bash
source venv/bin/activate
```

### Deactivate Environment

```bash
deactivate
```

### Install New Package

```bash
# Activate environment first
source venv/bin/activate

# Install package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt
```

### Start Jupyter Lab Manually

```bash
source venv/bin/activate
jupyter lab
```

### Start Jupyter Notebook (classic)

```bash
source venv/bin/activate
jupyter notebook
```

---

## Troubleshooting

### Script won't run: "Permission denied"

**Fix:**
```bash
chmod +x scripts/*.sh
```

### "Command not found: jupyter"

**Fix:**
```bash
source venv/bin/activate
pip install jupyter jupyterlab
```

### "ModuleNotFoundError" when running notebooks

**Fix:**
```bash
# Reinstall dependencies
source venv/bin/activate
pip install -r requirements.txt
```

### Virtual environment corrupted

**Fix:**
```bash
# Remove and recreate
rm -rf venv
./scripts/setup_local_env.sh
```

### Jupyter kernel not showing up

**Fix:**
```bash
source venv/bin/activate
python -m ipykernel install --user --name=cophil-training --display-name "Python (CoPhil)"
```

---

## Directory Structure

```
cophil-training-v1.0/
├── venv/                          # Virtual environment (ignored by git)
├── scripts/
│   ├── setup_local_env.sh        # Setup script
│   ├── start_jupyter.sh          # Start Jupyter Lab
│   ├── test_notebooks.sh         # Test notebooks
│   └── README.md                 # This file
├── day1/notebooks/               # Day 1 notebooks
├── day2/notebooks/               # Day 2 notebooks
├── requirements.txt              # Python dependencies
└── LOCAL_TESTING_SETUP.md        # Detailed setup guide
```

---

## Best Practices

### Before Committing

```bash
# 1. Test notebooks
./scripts/test_notebooks.sh

# 2. Check git status
git status

# 3. Review changes
git diff

# 4. Commit
git add .
git commit -m "Update notebooks"
git push
```

### Daily Workflow

```bash
# Morning: Start environment
./scripts/start_jupyter.sh

# Work on notebooks in browser...

# Evening: Test and commit
./scripts/test_notebooks.sh
git add day1/notebooks/*.ipynb
git commit -m "Fix: ..."
git push
```

### When Dependencies Change

```bash
# Update requirements.txt
source venv/bin/activate
pip install new-package
pip freeze > requirements.txt

# Commit changes
git add requirements.txt
git commit -m "Add new-package dependency"
```

---

## Performance Tips

### Speed up setup

Use pip cache:
```bash
pip install --cache-dir ~/.cache/pip -r requirements.txt
```

### Speed up testing

Test only changed notebooks:
```bash
# Get changed notebooks
git diff --name-only | grep .ipynb

# Test specific one
./scripts/test_notebooks.sh day1/notebooks/changed.ipynb
```

---

## See Also

- **Detailed guide:** `LOCAL_TESTING_SETUP.md`
- **GitHub Actions optimization:** `GITHUB_ACTIONS_OPTIMIZATION.md`
- **Project README:** `README.md`

---

*Last updated: 2025-10-20*
