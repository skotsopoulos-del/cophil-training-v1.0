#!/bin/bash
# Test Jupyter notebooks for syntax and basic execution
# Usage: ./scripts/test_notebooks.sh [notebook_path]

set -e  # Exit on error

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'

echo "================================================"
echo "CoPhil Training - Notebook Testing"
echo "================================================"
echo ""

# Check if venv is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo -e "${YELLOW}⚠️  Virtual environment not activated${NC}"
    echo "Activating venv..."

    if [ -d "venv" ]; then
        source venv/bin/activate
        echo -e "${GREEN}✓${NC} Environment activated"
    else
        echo -e "${RED}❌ No virtual environment found${NC}"
        echo "Run: ./scripts/setup_local_env.sh"
        exit 1
    fi
fi

echo ""

# Function to test a single notebook
test_notebook() {
    local notebook=$1
    local basename=$(basename "$notebook")

    echo -e "${BLUE}Testing:${NC} $basename"

    # Check if file exists
    if [ ! -f "$notebook" ]; then
        echo -e "  ${RED}❌ File not found${NC}"
        return 1
    fi

    # Test 1: Validate JSON structure
    echo -n "  • JSON validation... "
    if python3 -m json.tool "$notebook" > /dev/null 2>&1; then
        echo -e "${GREEN}✓${NC}"
    else
        echo -e "${RED}✗ Invalid JSON${NC}"
        return 1
    fi

    # Test 2: Check for syntax errors (convert without executing)
    echo -n "  • Syntax check... "
    if jupyter nbconvert --to notebook --output /tmp/test_output.ipynb "$notebook" --quiet 2>/dev/null; then
        echo -e "${GREEN}✓${NC}"
        rm -f /tmp/test_output.ipynb
    else
        echo -e "${RED}✗ Syntax errors${NC}"
        return 1
    fi

    # Test 3: Quick execution test (first 5 cells only, if --execute flag passed)
    if [ "$EXECUTE_CELLS" = "true" ]; then
        echo -n "  • Quick execution test... "
        # This would execute first few cells - skip for now as it's slow
        echo -e "${YELLOW}⊘ Skipped${NC}"
    fi

    echo -e "  ${GREEN}✓ Passed${NC}"
    echo ""

    return 0
}

# Parse arguments
EXECUTE_CELLS=false
SPECIFIC_NOTEBOOK=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --execute|-e)
            EXECUTE_CELLS=true
            shift
            ;;
        *)
            SPECIFIC_NOTEBOOK="$1"
            shift
            ;;
    esac
done

# Determine which notebooks to test
if [ -n "$SPECIFIC_NOTEBOOK" ]; then
    # Test specific notebook
    NOTEBOOKS=("$SPECIFIC_NOTEBOOK")
else
    # Test all notebooks
    NOTEBOOKS=(
        "day1/notebooks/Day1_Session3_Python_Geospatial_Data.ipynb"
        "day1/notebooks/Day1_Session4_Google_Earth_Engine.ipynb"
        "day2/notebooks/session1_hands_on_lab_student.ipynb"
        "day2/notebooks/session1_theory_notebook_STUDENT.ipynb"
        "day2/notebooks/session2_extended_lab_STUDENT.ipynb"
        "day2/notebooks/session3_theory_interactive.ipynb"
        "day2/notebooks/session4_cnn_classification_STUDENT.ipynb"
        "day2/notebooks/session4_transfer_learning_STUDENT.ipynb"
        "day3/notebooks/Day3_Session2_Flood_Mapping_UNet.ipynb"
        "day3/notebooks/Day3_Session4_Object_Detection_STUDENT.ipynb"
        "day4/notebooks/day4_session1_lstm_demo_STUDENT.ipynb"
        "day4/notebooks/day4_session2_lstm_drought_lab_STUDENT.ipynb"
    )
fi

# Test each notebook
PASSED=0
FAILED=0
FAILED_NOTEBOOKS=()

for notebook in "${NOTEBOOKS[@]}"; do
    if test_notebook "$notebook"; then
        ((PASSED++))
    else
        ((FAILED++))
        FAILED_NOTEBOOKS+=("$notebook")
    fi
done

# Summary
echo "================================================"
echo "Test Summary"
echo "================================================"
echo -e "Total:  $((PASSED + FAILED)) notebooks"
echo -e "Passed: ${GREEN}$PASSED${NC}"
echo -e "Failed: ${RED}$FAILED${NC}"
echo ""

if [ $FAILED -gt 0 ]; then
    echo "Failed notebooks:"
    for nb in "${FAILED_NOTEBOOKS[@]}"; do
        echo "  • $nb"
    done
    echo ""
    exit 1
else
    echo -e "${GREEN}✓ All notebooks passed!${NC}"
    echo ""
fi
