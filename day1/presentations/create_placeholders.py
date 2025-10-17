#!/usr/bin/env python3
"""
Create placeholder images for Day 1 presentations
This allows presentations to render without 404 errors while sourcing real images
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder(filename, text, size=(1920, 1080), bg_color='#1e3a8a'):
    """Create a simple placeholder image with centered text"""
    img = Image.new('RGB', size, color=bg_color)
    d = ImageDraw.Draw(img)
    
    # Try to use a system font, fallback to default
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 60)
        small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 30)
    except:
        try:
            font = ImageFont.truetype("Arial.ttf", 60)
            small_font = ImageFont.truetype("Arial.ttf", 30)
        except:
            font = ImageFont.load_default()
            small_font = ImageFont.load_default()
    
    # Main text
    bbox = d.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((size[0] - text_width) / 2, (size[1] - text_height) / 2 - 50)
    d.text(position, text, fill='white', font=font)
    
    # Placeholder label
    label = "[PLACEHOLDER IMAGE]"
    bbox2 = d.textbbox((0, 0), label, font=small_font)
    label_width = bbox2[2] - bbox2[0]
    label_pos = ((size[0] - label_width) / 2, position[1] + text_height + 30)
    d.text(label_pos, label, fill='#a0a0a0', font=small_font)
    
    # Save
    os.makedirs('images', exist_ok=True)
    img.save(f'images/{filename}')
    return filename

# All images referenced in presentations
images = [
    # Session 1: Copernicus & Philippine EO
    ('eu_global_gateway.png', 'EU Global Gateway', (800, 400)),
    ('copphil_logo.png', 'CoPhil Logo', (400, 200)),
    ('philsa_logo.png', 'PhilSA Logo', (400, 200)),
    ('dost_logo.png', 'DOST Logo', (400, 200)),
    ('copernicus_overview.jpg', 'Copernicus Programme'),
    ('copernicus_applications.png', 'Copernicus Applications'),
    ('sentinel1_satellite.jpg', 'Sentinel-1 SAR Satellite'),
    ('sar_principle.png', 'SAR Imaging Principle'),
    ('polarization_comparison.jpg', 'VV vs VH Polarization'),
    ('s1_flood_mapping.jpg', 'Flood Mapping with SAR'),
    ('s1_insar.jpg', 'InSAR Ground Deformation'),
    ('sentinel1_flood_ph.png', 'Philippine Flood Example'),
    ('sentinel2_mayon.jpg', 'Sentinel-2: Mayon Volcano'),
    ('s1_s2_synergy.jpg', 'SAR + Optical Synergy'),
    ('dataspace_portal.jpg', 'Copernicus Data Space'),
    ('sentiboard.jpg', 'SentiBoard Platform'),
    ('gee_logo.png', 'Google Earth Engine', (400, 200)),
    ('ph_eo_ecosystem.png', 'Philippine EO Ecosystem'),
    ('philsa_building.jpg', 'PhilSA Headquarters'),
    ('siyasat_portal.jpg', 'SIYASAT Data Portal'),
    ('space_plus_dashboard.jpg', 'Space+ Dashboard'),
    ('coare_infrastructure.jpg', 'COARE HPC Infrastructure'),
    ('namria_logo.png', 'NAMRIA Logo', (400, 200)),
    ('namria_geoportal.jpg', 'NAMRIA Geoportal'),
    ('namria_landcover.jpg', 'NAMRIA Land Cover Map'),
    ('hazardhunter.jpg', 'HazardHunter Platform'),
    ('dost_asti_logo.png', 'DOST-ASTI Logo', (400, 200)),
    ('datos_logo.png', 'DATOS Logo', (400, 200)),
    ('skai_pinas.jpg', 'SkAI-Pinas Programme'),
    ('dimer_interface.jpg', 'DIMER Platform'),
    ('aipi_workflow.png', 'AIPI Workflow'),
    ('asti_ecosystem.png', 'ASTI Platform Ecosystem'),
    ('pagasa_logo.png', 'PAGASA Logo', (400, 200)),
    ('mirror_site_concept.jpg', 'Mirror Site Architecture'),
    ('digital_campus.jpg', 'Digital Campus Concept'),
    ('integration_diagram.png', 'Platform Integration'),
    
    # Session 2: AI/ML Fundamentals
    ('ai_ml_dl_venn.png', 'AI / ML / DL Relationship'),
    ('ml_definition.png', 'Machine Learning Definition'),
    ('traditional_vs_ml.png', 'Traditional vs ML'),
    ('eo_ml_workflow.png', 'EO ML Workflow'),
    ('problem_formulation.png', 'Problem Formulation'),
    ('data_collection_eo.png', 'EO Data Collection'),
    ('preprocessing_pipeline.png', 'Preprocessing Pipeline'),
    ('feature_engineering.jpg', 'Feature Engineering'),
    ('model_training.png', 'Model Training Process'),
    ('validation_workflow.png', 'Validation Methodology'),
    ('deployment_architecture.png', 'Deployment Architecture'),
    ('supervised_learning_concept.png', 'Supervised Learning'),
    ('classification_example.jpg', 'Land Cover Classification'),
    ('regression_example.png', 'Regression Example'),
    ('decision_boundary.png', 'Decision Boundary'),
    ('random_forest_diagram.png', 'Random Forest'),
    ('confusion_matrix.png', 'Confusion Matrix'),
    ('unsupervised_concept.png', 'Unsupervised Learning'),
    ('clustering_example.jpg', 'K-means Clustering'),
    ('anomaly_detection.jpg', 'Anomaly Detection'),
    ('neural_network_diagram.png', 'Neural Network'),
    ('cnn_architecture.png', 'CNN Architecture'),
    ('convolution_operation.gif', 'Convolution Operation', (800, 600)),
    ('pooling_operation.png', 'Pooling Operation'),
    ('unet_architecture.png', 'U-Net Architecture'),
    ('semantic_segmentation.jpg', 'Semantic Segmentation'),
    ('model_centric_vs_data_centric.png', 'Model vs Data Centric'),
    ('data_quality_impact.png', 'Data Quality Impact'),
    ('labeling_quality.jpg', 'Labeling Quality'),
    ('active_learning_loop.png', 'Active Learning'),
    ('foundation_models_timeline.png', 'Foundation Models 2025'),
    ('prithvi_architecture.png', 'Prithvi Architecture'),
    ('clay_model_overview.png', 'Clay Model'),
    ('nasa_ibm_logo.png', 'NASA-IBM Partnership', (600, 300)),
    ('foundation_model_benefits.png', 'Foundation Model Benefits'),
    ('fine_tuning_workflow.png', 'Fine-tuning Workflow'),
    ('phisat2_satellite.jpg', 'Φsat-2 Satellite'),
    ('onboard_ai_concept.png', 'On-board AI Processing'),
    ('edge_computing_diagram.png', 'Edge Computing'),
    ('ph_flood_ml.jpg', 'Philippine Flood ML'),
    ('typhoon_damage_assessment.jpg', 'Typhoon Damage Assessment'),
    ('rice_monitoring_ph.jpg', 'Rice Monitoring'),
    ('mangrove_mapping.jpg', 'Mangrove Classification'),
    
    # Session 3: Python Geospatial
    ('geopandas_logo.png', 'GeoPandas', (400, 200)),
    ('rasterio_logo.png', 'Rasterio', (400, 200)),
    ('python_geospatial_stack.png', 'Python GIS Stack'),
    ('colab_interface.jpg', 'Google Colab'),
    
    # Session 4: Google Earth Engine
    ('gee_architecture.png', 'GEE Architecture'),
    ('geemap_logo.png', 'geemap Library', (400, 200)),
]

def main():
    print("Creating placeholder images for Day 1 presentations...")
    print("=" * 60)
    
    created = 0
    skipped = 0
    
    for img_data in images:
        filename = img_data[0]
        text = img_data[1]
        size = img_data[2] if len(img_data) > 2 else (1920, 1080)
        
        # Skip if already exists
        if os.path.exists(f'images/{filename}'):
            print(f"⏭️  Skipping (exists): {filename}")
            skipped += 1
            continue
        
        create_placeholder(filename, text, size)
        print(f"✅ Created: {filename}")
        created += 1
    
    print("=" * 60)
    print(f"✅ Created: {created} placeholder images")
    print(f"⏭️  Skipped: {skipped} existing images")
    print(f"📁 Location: course_site/day1/presentations/images/")
    print()
    print("⚠️  NOTE: These are PLACEHOLDER images only!")
    print("   Replace with real images before final delivery.")
    print("   See IMAGE_PLACEHOLDERS.md for sourcing guidance.")

if __name__ == '__main__':
    main()
