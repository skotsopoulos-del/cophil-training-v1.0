#!/bin/bash
# Quick start script for Jupyter Lab
# Usage: ./scripts/start_jupyter.sh

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo "================================================"
echo "Starting Jupyter Lab"
echo "================================================"
echo ""

# Check if venv exists
if [ ! -d "venv" ]; then
    echo -e "${RED}❌ Virtual environment not found${NC}"
    echo "Run setup first: ./scripts/setup_local_env.sh"
    exit 1
fi

# Activate venv
echo "Activating virtual environment..."
source venv/bin/activate
echo -e "${GREEN}✓${NC} Environment activated"
echo ""

# Check if jupyter is installed
if ! command -v jupyter &> /dev/null; then
    echo -e "${RED}❌ Jupyter not installed${NC}"
    echo "Run setup first: ./scripts/setup_local_env.sh"
    exit 1
fi

# Start Jupyter Lab
echo "Starting Jupyter Lab..."
echo "Browser will open automatically at http://localhost:8888"
echo ""
echo -e "${YELLOW}Press Ctrl+C to stop Jupyter Lab${NC}"
echo ""

# Open browser after 2 seconds
(sleep 2 && open http://localhost:8888) &

# Start jupyter lab
jupyter lab
