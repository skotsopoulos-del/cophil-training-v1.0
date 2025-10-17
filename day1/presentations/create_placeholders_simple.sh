#!/bin/bash
# Create simple placeholder images using ImageMagick (if available) or touch empty files

echo "Creating placeholder images for Day 1 presentations..."
echo "========================================================"

# Create images directory
mkdir -p images

# Array of all image files needed
images=(
    # Session 1
    "eu_global_gateway.png" "copphil_logo.png" "philsa_logo.png" "dost_logo.png"
    "copernicus_overview.jpg" "copernicus_applications.png" "sentinel1_satellite.jpg"
    "sar_principle.png" "polarization_comparison.jpg" "s1_flood_mapping.jpg"
    "s1_insar.jpg" "sentinel1_flood_ph.png" "sentinel2_mayon.jpg" "s1_s2_synergy.jpg"
    "dataspace_portal.jpg" "sentiboard.jpg" "gee_logo.png" "ph_eo_ecosystem.png"
    "philsa_building.jpg" "siyasat_portal.jpg" "space_plus_dashboard.jpg"
    "coare_infrastructure.jpg" "namria_logo.png" "namria_geoportal.jpg"
    "namria_landcover.jpg" "hazardhunter.jpg" "dost_asti_logo.png" "datos_logo.png"
    "skai_pinas.jpg" "dimer_interface.jpg" "aipi_workflow.png" "asti_ecosystem.png"
    "pagasa_logo.png" "mirror_site_concept.jpg" "digital_campus.jpg" "integration_diagram.png"
    
    # Session 2
    "ai_ml_dl_venn.png" "ml_definition.png" "traditional_vs_ml.png" "eo_ml_workflow.png"
    "problem_formulation.png" "data_collection_eo.png" "preprocessing_pipeline.png"
    "feature_engineering.jpg" "model_training.png" "validation_workflow.png"
    "deployment_architecture.png" "supervised_learning_concept.png" "classification_example.jpg"
    "regression_example.png" "decision_boundary.png" "random_forest_diagram.png"
    "confusion_matrix.png" "unsupervised_concept.png" "clustering_example.jpg"
    "anomaly_detection.jpg" "neural_network_diagram.png" "cnn_architecture.png"
    "convolution_operation.gif" "pooling_operation.png" "unet_architecture.png"
    "semantic_segmentation.jpg" "model_centric_vs_data_centric.png" "data_quality_impact.png"
    "labeling_quality.jpg" "active_learning_loop.png" "foundation_models_timeline.png"
    "prithvi_architecture.png" "clay_model_overview.png" "nasa_ibm_logo.png"
    "foundation_model_benefits.png" "fine_tuning_workflow.png" "phisat2_satellite.jpg"
    "onboard_ai_concept.png" "edge_computing_diagram.png" "ph_flood_ml.jpg"
    "typhoon_damage_assessment.jpg" "rice_monitoring_ph.jpg" "mangrove_mapping.jpg"
    
    # Session 3
    "geopandas_logo.png" "rasterio_logo.png" "python_geospatial_stack.png" "colab_interface.jpg"
    
    # Session 4
    "gee_architecture.png" "geemap_logo.png"
)

# Check if ImageMagick is available
if command -v convert &> /dev/null; then
    echo "✅ ImageMagick found - creating placeholder images with text"
    for img in "${images[@]}"; do
        if [ ! -f "images/$img" ]; then
            # Extract name without extension for label
            name=$(basename "$img" | sed 's/\.[^.]*$//')
            # Create a simple placeholder with text
            convert -size 1920x1080 xc:'#1e3a8a' \
                    -gravity center \
                    -pointsize 60 -fill white -annotate +0-50 "$name" \
                    -pointsize 30 -fill gray -annotate +0+50 "[PLACEHOLDER]" \
                    "images/$img" 2>/dev/null && echo "✅ Created: $img" || echo "⚠️  Could not create: $img"
        else
            echo "⏭️  Skipping (exists): $img"
        fi
    done
else
    echo "⚠️  ImageMagick not found - creating empty placeholder files"
    echo "   (Images will still show as 404, but files will exist)"
    for img in "${images[@]}"; do
        if [ ! -f "images/$img" ]; then
            touch "images/$img"
            echo "✅ Created empty: $img"
        else
            echo "⏭️  Skipping (exists): $img"
        fi
    done
    echo ""
    echo "💡 To create actual placeholder images:"
    echo "   1. Install Pillow: pip install Pillow"
    echo "   2. Run: python3 create_placeholders.py"
    echo "   OR install ImageMagick: brew install imagemagick"
fi

echo ""
echo "========================================================"
echo "✅ Placeholder setup complete!"
echo "📁 Location: course_site/day1/presentations/images/"
echo ""
echo "⚠️  IMPORTANT: These are PLACEHOLDER images only!"
echo "   See IMAGE_PLACEHOLDERS.md for real image sources."
echo "   Presentations will render, but images won't be meaningful."
