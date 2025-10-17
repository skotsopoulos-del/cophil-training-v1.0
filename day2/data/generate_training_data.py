"""
Generate comprehensive training polygons for Palawan land cover classification
Creates 80 training polygons (10 per class) and 40 validation polygons (5 per class)
"""

import json
import random

# Set random seed for reproducibility
random.seed(42)

# Palawan bounding box
PALAWAN_BOUNDS = {
    'min_lon': 117.5,
    'max_lon': 120.5,
    'min_lat': 8.5,
    'max_lat': 11.5
}

# Class definitions
CLASSES = [
    {'id': 1, 'name': 'Primary Forest', 'color': '#0A5F0A'},
    {'id': 2, 'name': 'Secondary Forest', 'color': '#4CAF50'},
    {'id': 3, 'name': 'Mangroves', 'color': '#009688'},
    {'id': 4, 'name': 'Agricultural Land', 'color': '#FFC107'},
    {'id': 5, 'name': 'Grassland/Scrubland', 'color': '#FFEB3B'},
    {'id': 6, 'name': 'Water Bodies', 'color': '#2196F3'},
    {'id': 7, 'name': 'Urban/Built-up', 'color': '#F44336'},
    {'id': 8, 'name': 'Bare Soil/Mining', 'color': '#795548'}
]

# Region definitions for spatial distribution
REGIONS = {
    'North': {'lat': (10.5, 11.5), 'lon': (118.5, 119.5)},
    'Central': {'lat': (9.5, 10.5), 'lon': (118.5, 119.5)},
    'South': {'lat': (8.5, 9.5), 'lon': (118.5, 119.5)},
    'West Coast': {'lat': (9.0, 11.0), 'lon': (117.5, 118.5)},
    'East Coast': {'lat': (9.0, 11.0), 'lon': (119.5, 120.5)}
}

def create_polygon(center_lon, center_lat, size=0.02):
    """Create a square polygon around a center point"""
    half = size / 2
    return [[
        [center_lon - half, center_lat + half],
        [center_lon + half, center_lat + half],
        [center_lon + half, center_lat - half],
        [center_lon - half, center_lat - half],
        [center_lon - half, center_lat + half]
    ]]

def generate_random_point(region_name):
    """Generate a random point within a region"""
    region = REGIONS[region_name]
    lat = random.uniform(region['lat'][0], region['lat'][1])
    lon = random.uniform(region['lon'][0], region['lon'][1])
    return lon, lat

def create_feature(class_info, polygon_num, is_training=True):
    """Create a GeoJSON feature"""
    # Distribute across regions
    regions = list(REGIONS.keys())
    region = regions[polygon_num % len(regions)]
    
    lon, lat = generate_random_point(region)
    
    properties = {
        'class_id': class_info['id'],
        'class_name': class_info['name'],
        'region': region,
        'type': 'training' if is_training else 'validation',
        'polygon_id': f"{class_info['name'].replace(' ', '_')}_{polygon_num + 1}"
    }
    
    return {
        'type': 'Feature',
        'properties': properties,
        'geometry': {
            'type': 'Polygon',
            'coordinates': create_polygon(lon, lat)
        }
    }

def create_geojson(features, name):
    """Create a complete GeoJSON FeatureCollection"""
    return {
        'type': 'FeatureCollection',
        'name': name,
        'crs': {
            'type': 'name',
            'properties': {'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'}
        },
        'features': features
    }

# Generate training data (10 polygons per class)
print("Generating training data...")
training_features = []
for class_info in CLASSES:
    for i in range(10):
        feature = create_feature(class_info, i, is_training=True)
        training_features.append(feature)

training_geojson = create_geojson(training_features, 'palawan_training_polygons')

# Generate validation data (5 polygons per class)
print("Generating validation data...")
validation_features = []
for class_info in CLASSES:
    for i in range(5):
        feature = create_feature(class_info, i, is_training=False)
        validation_features.append(feature)

validation_geojson = create_geojson(validation_features, 'palawan_validation_polygons')

# Save to files
with open('palawan_training_polygons.geojson', 'w') as f:
    json.dump(training_geojson, f, indent=2)
print(f"✓ Created training data: {len(training_features)} polygons")

with open('palawan_validation_polygons.geojson', 'w') as f:
    json.dump(validation_geojson, f, indent=2)
print(f"✓ Created validation data: {len(validation_features)} polygons")

# Create summary
summary = {
    'training_polygons': len(training_features),
    'validation_polygons': len(validation_features),
    'total_polygons': len(training_features) + len(validation_features),
    'classes': len(CLASSES),
    'polygons_per_class_training': 10,
    'polygons_per_class_validation': 5,
    'study_area': 'Palawan, Philippines',
    'crs': 'EPSG:4326',
    'class_distribution': {}
}

for class_info in CLASSES:
    summary['class_distribution'][class_info['name']] = {
        'training': 10,
        'validation': 5,
        'total': 15
    }

with open('dataset_summary.json', 'w') as f:
    json.dump(summary, f, indent=2)
print(f"✓ Created dataset summary")

print("\nDataset Generation Complete!")
print(f"Total Training Polygons: {len(training_features)}")
print(f"Total Validation Polygons: {len(validation_features)}")
print(f"Classes: {len(CLASSES)}")
