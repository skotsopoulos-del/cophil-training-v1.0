#!/bin/bash
# Setup script for local Jupyter notebook testing environment
# Usage: ./scripts/setup_local_env.sh

set -e  # Exit on error

echo "================================================"
echo "CoPhil Training - Local Environment Setup"
echo "================================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if Python 3 is installed
echo "1. Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 is not installed${NC}"
    echo "Please install Python 3.11+ from https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | awk '{print $2}')
echo -e "${GREEN}✓${NC} Python $PYTHON_VERSION found"

# Check Python version (should be 3.11+)
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 11 ]); then
    echo -e "${YELLOW}⚠️  Warning: Python 3.11+ recommended (you have $PYTHON_VERSION)${NC}"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo ""

# Check if venv exists
echo "2. Setting up virtual environment..."
if [ -d "venv" ]; then
    echo -e "${YELLOW}⚠️  Virtual environment already exists${NC}"
    read -p "Remove and recreate? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Removing existing venv..."
        rm -rf venv
    else
        echo "Skipping venv creation"
        source venv/bin/activate
    fi
fi

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo -e "${GREEN}✓${NC} Virtual environment created"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo -e "${GREEN}✓${NC} Virtual environment activated"

echo ""

# Upgrade pip
echo "3. Upgrading pip..."
pip install --upgrade pip --quiet
echo -e "${GREEN}✓${NC} pip upgraded"

echo ""

# Install requirements
echo "4. Installing project dependencies..."
echo "This may take 5-15 minutes depending on your internet connection..."
echo ""

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt --quiet
    echo -e "${GREEN}✓${NC} Project dependencies installed"
else
    echo -e "${RED}❌ requirements.txt not found${NC}"
    exit 1
fi

echo ""

# Install Jupyter and extensions
echo "5. Installing Jupyter Lab and extensions..."
pip install jupyter jupyterlab ipywidgets nbformat nbconvert ipykernel --quiet
echo -e "${GREEN}✓${NC} Jupyter Lab installed"

echo ""

# Register Jupyter kernel
echo "6. Registering Jupyter kernel..."
python -m ipykernel install --user --name=cophil-training --display-name "Python (CoPhil)" 2>/dev/null || true
echo -e "${GREEN}✓${NC} Kernel registered"

echo ""

# Verify installations
echo "7. Verifying installations..."
echo ""

REQUIRED_PACKAGES=(
    "numpy"
    "pandas"
    "matplotlib"
    "geopandas"
    "rasterio"
    "earthengine-api"
    "jupyter"
    "jupyterlab"
)

ALL_INSTALLED=true
for package in "${REQUIRED_PACKAGES[@]}"; do
    if pip list | grep -q "^$package "; then
        VERSION=$(pip show $package | grep "^Version:" | awk '{print $2}')
        echo -e "  ${GREEN}✓${NC} $package ($VERSION)"
    else
        echo -e "  ${RED}❌${NC} $package (missing)"
        ALL_INSTALLED=false
    fi
done

echo ""

if [ "$ALL_INSTALLED" = false ]; then
    echo -e "${RED}❌ Some packages failed to install${NC}"
    echo "Try running: pip install -r requirements.txt"
    exit 1
fi

echo ""
echo "================================================"
echo -e "${GREEN}✓ Setup complete!${NC}"
echo "================================================"
echo ""
echo "To start working:"
echo "  1. Activate environment:  source venv/bin/activate"
echo "  2. Start Jupyter Lab:     jupyter lab"
echo "  3. Open a notebook and start testing!"
echo ""
echo "To deactivate later:       deactivate"
echo ""
echo "For more information, see: LOCAL_TESTING_SETUP.md"
echo ""
