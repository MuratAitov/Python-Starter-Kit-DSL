# 🗺️ Mapping & GIS Templates

Create interactive maps and visualize geographic data.

## What You Can Build

- **Interactive maps** — Plot locations with markers
- **Data visualization** — Show data on maps (choropleth)
- **Route mapping** — Display paths and journeys
- **Historical maps** — Visualize historical locations
- **Cluster maps** — Group nearby points

---

## Available Templates

### 1. `simple_map.py` — Basic Map Creator (Streamlit App)
An easy web app to create maps with markers.

**Features:**
- Add locations by address or coordinates
- Customize markers with colors and popups
- Save maps as HTML files
- Upload CSV with locations

**How to use:**

1. **Run the app:**
   ```bash
   streamlit run templates/mapping_templates/simple_map.py
   ```

2. **Add locations** manually or upload a CSV file

3. **Download** your map as an HTML file

---

### 2. `map_from_csv.py` — Map Data from Spreadsheet
A script to create maps from CSV files with coordinates.

**Features:**
- Read locations from CSV/Excel
- Auto-detect lat/long columns
- Create clustered markers
- Export to HTML

**How to use:**

1. **Prepare your data** with latitude/longitude columns

2. **Run the script:**
   ```bash
   python templates/mapping_templates/map_from_csv.py
   ```

---

## Example Ideas

### Simple Ideas (Beginners)
- **Travel Map** — Mark places you've visited
- **Store Locator** — Show business locations
- **Event Map** — Map event locations
- **Campus Map** — Mark buildings on campus

### Medium Ideas
- **Historical Journey** — Trace a historical route
- **Research Sites** — Map field study locations
- **Data by Region** — Color regions by data values
- **Timeline Map** — Show location changes over time

### Advanced Ideas
- **Heat Maps** — Show data density
- **Migration Patterns** — Visualize movement data
- **Spatial Analysis** — Analyze geographic relationships
- **Story Maps** — Narrative maps with multimedia

---

## Quick Tips

### Create a Basic Map
```python
import folium

# Create map centered on a location
m = folium.Map(
    location=[40.7128, -74.0060],  # NYC coordinates
    zoom_start=12
)

# Save to HTML
m.save('my_map.html')
```

### Add Markers
```python
import folium

m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

# Add a marker
folium.Marker(
    location=[40.7128, -74.0060],
    popup="New York City",
    tooltip="Click me!",
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(m)

m.save('map_with_marker.html')
```

### Add Multiple Markers from Data
```python
import folium
import pandas as pd

# Sample data
data = pd.DataFrame({
    'name': ['NYC', 'LA', 'Chicago'],
    'lat': [40.7128, 34.0522, 41.8781],
    'lon': [-74.0060, -118.2437, -87.6298]
})

# Create map
m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

# Add markers for each location
for idx, row in data.iterrows():
    folium.Marker(
        location=[row['lat'], row['lon']],
        popup=row['name']
    ).add_to(m)

m.save('multi_marker_map.html')
```

### Cluster Markers (for many points)
```python
from folium.plugins import MarkerCluster

m = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
marker_cluster = MarkerCluster().add_to(m)

# Add markers to cluster
for lat, lon, name in locations:
    folium.Marker(
        location=[lat, lon],
        popup=name
    ).add_to(marker_cluster)

m.save('clustered_map.html')
```

### Create Choropleth (colored regions)
```python
import folium
import pandas as pd

# Load geographic boundaries (GeoJSON)
# You can find state/country GeoJSON files online

m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

folium.Choropleth(
    geo_data='us-states.json',  # GeoJSON file
    data=state_data,            # Your DataFrame
    columns=['State', 'Value'], # Columns to use
    key_on='feature.id',        # GeoJSON property to match
    fill_color='YlOrRd',        # Color scale
    legend_name='Data Values'
).add_to(m)

m.save('choropleth_map.html')
```

### Add Circle Markers (sized by data)
```python
for idx, row in data.iterrows():
    folium.CircleMarker(
        location=[row['lat'], row['lon']],
        radius=row['value'] / 10,  # Size based on data
        popup=row['name'],
        color='blue',
        fill=True
    ).add_to(m)
```

---

## Geocoding (Address to Coordinates)

### Using Geopy
```python
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_app")

# Get coordinates from address
location = geolocator.geocode("1600 Pennsylvania Ave, Washington DC")

print(f"Latitude: {location.latitude}")
print(f"Longitude: {location.longitude}")
```

### Batch Geocoding
```python
import time
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_app")

addresses = ["New York, NY", "Los Angeles, CA", "Chicago, IL"]
coordinates = []

for address in addresses:
    location = geolocator.geocode(address)
    if location:
        coordinates.append({
            'address': address,
            'lat': location.latitude,
            'lon': location.longitude
        })
    time.sleep(1)  # Be respectful - wait between requests
```

---

## Common Issues

### "Module not found: folium"
```bash
pip install folium
```

### "Module not found: geopy"
```bash
pip install geopy
```

### Map doesn't display
- Make sure you're opening the HTML file in a browser
- For Streamlit, use `st_folium` or `st.components.v1.html`

### Geocoding rate limits
```python
# Add delays between requests
import time
time.sleep(1)  # Wait 1 second

# Or use a different geocoding service
```

### Map centers on wrong location
```python
# Calculate center from your data
center_lat = data['lat'].mean()
center_lon = data['lon'].mean()

m = folium.Map(location=[center_lat, center_lon], zoom_start=10)
```

---

## Map Tile Styles

```python
# Different map styles
folium.Map(location=[lat, lon], tiles='OpenStreetMap')  # Default
folium.Map(location=[lat, lon], tiles='CartoDB positron')  # Light
folium.Map(location=[lat, lon], tiles='CartoDB dark_matter')  # Dark
folium.Map(location=[lat, lon], tiles='Stamen Terrain')  # Terrain
folium.Map(location=[lat, lon], tiles='Stamen Watercolor')  # Artistic
```

---

## Learn More

- [Folium Documentation](https://python-visualization.github.io/folium/)
- [Folium Quickstart](https://python-visualization.github.io/folium/quickstart.html)
- [Geopy Documentation](https://geopy.readthedocs.io/)
- [GeoJSON Data Sources](https://github.com/datasets/geo-countries)

---

**Need help?** Ask your instructor or check the main README.md
