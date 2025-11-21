"""
Simple Map Creator - Streamlit Web App
Create interactive maps with markers.

Run with: streamlit run templates/mapping_templates/simple_map.py
"""

import streamlit as st
import pandas as pd

# Try to import folium
try:
    import folium
    from folium.plugins import MarkerCluster
    from streamlit_folium import st_folium
    FOLIUM_AVAILABLE = True
except ImportError:
    FOLIUM_AVAILABLE = False

# Try to import geopy for geocoding
try:
    from geopy.geocoders import Nominatim
    from geopy.exc import GeocoderTimedOut
    GEOPY_AVAILABLE = True
except ImportError:
    GEOPY_AVAILABLE = False

# Page configuration
st.set_page_config(
    page_title="Map Creator",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ Interactive Map Creator")
st.write("Create maps with markers from addresses or coordinates!")

# Check dependencies
if not FOLIUM_AVAILABLE:
    st.error("Required libraries not installed. Run:")
    st.code("pip install folium streamlit-folium")
    st.stop()

# Initialize session state for locations
if 'locations' not in st.session_state:
    st.session_state['locations'] = []

# --- Sidebar ---
st.sidebar.header("Map Settings")

# Map style
map_style = st.sidebar.selectbox(
    "Map Style",
    ["OpenStreetMap", "CartoDB positron", "CartoDB dark_matter"]
)

# Default center
default_lat = st.sidebar.number_input("Default Latitude", value=39.8283)
default_lon = st.sidebar.number_input("Default Longitude", value=-98.5795)
default_zoom = st.sidebar.slider("Default Zoom", 1, 18, 4)

# --- Main Interface ---
tab1, tab2, tab3 = st.tabs(["Add Locations", "View Map", "Export"])

# Tab 1: Add Locations
with tab1:
    st.header("Add Locations")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Add by Coordinates")

        with st.form("coord_form"):
            name = st.text_input("Location Name", placeholder="My Location")
            lat = st.number_input("Latitude", value=40.7128, format="%.6f")
            lon = st.number_input("Longitude", value=-74.0060, format="%.6f")
            color = st.selectbox("Marker Color",
                ["blue", "red", "green", "purple", "orange", "darkred", "lightblue", "pink"])

            if st.form_submit_button("Add Location"):
                st.session_state['locations'].append({
                    'name': name if name else f"Location {len(st.session_state['locations'])+1}",
                    'lat': lat,
                    'lon': lon,
                    'color': color
                })
                st.success(f"Added: {name}")

    with col2:
        st.subheader("Add by Address")

        if GEOPY_AVAILABLE:
            with st.form("address_form"):
                address = st.text_input("Address", placeholder="1600 Pennsylvania Ave, Washington DC")
                addr_name = st.text_input("Name (optional)", placeholder="White House")
                addr_color = st.selectbox("Color",
                    ["red", "blue", "green", "purple", "orange"], key="addr_color")

                if st.form_submit_button("Find & Add"):
                    if address:
                        with st.spinner("Finding location..."):
                            try:
                                geolocator = Nominatim(user_agent="dsl_map_creator")
                                location = geolocator.geocode(address, timeout=10)

                                if location:
                                    st.session_state['locations'].append({
                                        'name': addr_name if addr_name else address,
                                        'lat': location.latitude,
                                        'lon': location.longitude,
                                        'color': addr_color
                                    })
                                    st.success(f"Found: {location.address[:50]}...")
                                else:
                                    st.error("Address not found")
                            except GeocoderTimedOut:
                                st.error("Geocoding timed out. Try again.")
                            except Exception as e:
                                st.error(f"Error: {e}")
        else:
            st.warning("Install geopy for address lookup: `pip install geopy`")

    # Upload CSV
    st.subheader("Upload from CSV")
    st.write("CSV should have columns: `name`, `lat` (or `latitude`), `lon` (or `longitude`)")

    uploaded_file = st.file_uploader("Upload CSV", type=['csv'])

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)

            # Try to find lat/lon columns
            lat_col = None
            lon_col = None

            for col in df.columns:
                if col.lower() in ['lat', 'latitude']:
                    lat_col = col
                if col.lower() in ['lon', 'lng', 'longitude', 'long']:
                    lon_col = col

            if lat_col and lon_col:
                st.write(f"Found coordinates in columns: `{lat_col}`, `{lon_col}`")
                st.dataframe(df.head())

                if st.button("Add All Locations from CSV"):
                    name_col = 'name' if 'name' in df.columns else None

                    for idx, row in df.iterrows():
                        st.session_state['locations'].append({
                            'name': row[name_col] if name_col else f"Location {idx+1}",
                            'lat': row[lat_col],
                            'lon': row[lon_col],
                            'color': 'blue'
                        })

                    st.success(f"Added {len(df)} locations!")
            else:
                st.error("Could not find latitude/longitude columns")
        except Exception as e:
            st.error(f"Error reading CSV: {e}")

    # Current locations
    st.subheader("Current Locations")

    if st.session_state['locations']:
        df = pd.DataFrame(st.session_state['locations'])
        st.dataframe(df, use_container_width=True)

        if st.button("Clear All Locations"):
            st.session_state['locations'] = []
            st.rerun()
    else:
        st.info("No locations added yet")

# Tab 2: View Map
with tab2:
    st.header("Map Preview")

    if st.session_state['locations']:
        # Calculate center
        lats = [loc['lat'] for loc in st.session_state['locations']]
        lons = [loc['lon'] for loc in st.session_state['locations']]
        center_lat = sum(lats) / len(lats)
        center_lon = sum(lons) / len(lons)

        # Create map
        m = folium.Map(
            location=[center_lat, center_lon],
            zoom_start=default_zoom,
            tiles=map_style
        )

        # Add markers
        use_clusters = st.checkbox("Cluster nearby markers", value=len(st.session_state['locations']) > 20)

        if use_clusters:
            marker_cluster = MarkerCluster().add_to(m)
            target = marker_cluster
        else:
            target = m

        for loc in st.session_state['locations']:
            folium.Marker(
                location=[loc['lat'], loc['lon']],
                popup=f"<b>{loc['name']}</b><br>Lat: {loc['lat']:.4f}<br>Lon: {loc['lon']:.4f}",
                tooltip=loc['name'],
                icon=folium.Icon(color=loc['color'], icon='info-sign')
            ).add_to(target)

        # Display map
        st_folium(m, width=None, height=500)

        st.write(f"Showing {len(st.session_state['locations'])} location(s)")
    else:
        # Show empty map
        m = folium.Map(
            location=[default_lat, default_lon],
            zoom_start=default_zoom,
            tiles=map_style
        )
        st_folium(m, width=None, height=500)
        st.info("Add locations to see them on the map")

# Tab 3: Export
with tab3:
    st.header("Export")

    if st.session_state['locations']:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Download Locations (CSV)")
            df = pd.DataFrame(st.session_state['locations'])
            csv = df.to_csv(index=False)
            st.download_button(
                "Download CSV",
                csv,
                "locations.csv",
                "text/csv"
            )

        with col2:
            st.subheader("Download Map (HTML)")

            # Recreate map for download
            lats = [loc['lat'] for loc in st.session_state['locations']]
            lons = [loc['lon'] for loc in st.session_state['locations']]
            center_lat = sum(lats) / len(lats)
            center_lon = sum(lons) / len(lons)

            m = folium.Map(
                location=[center_lat, center_lon],
                zoom_start=default_zoom,
                tiles=map_style
            )

            for loc in st.session_state['locations']:
                folium.Marker(
                    location=[loc['lat'], loc['lon']],
                    popup=f"<b>{loc['name']}</b><br>Lat: {loc['lat']:.4f}<br>Lon: {loc['lon']:.4f}",
                    tooltip=loc['name'],
                    icon=folium.Icon(color=loc['color'], icon='info-sign')
                ).add_to(m)

            # Save to string
            map_html = m._repr_html_()

            st.download_button(
                "Download HTML Map",
                map_html,
                "my_map.html",
                "text/html"
            )
    else:
        st.info("Add locations first to export")

# --- Footer ---
st.markdown("---")
st.markdown("*Built with Streamlit & Folium | Digital Scholarship Lab Starter Kit*")
