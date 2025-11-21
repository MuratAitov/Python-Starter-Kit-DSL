"""
Simple Network Visualizer - Streamlit Web App
Create and visualize network graphs.

Run with: streamlit run templates/network_templates/simple_network.py
"""

import streamlit as st
import pandas as pd
import io

# Try to import network libraries
try:
    import networkx as nx
    NETWORKX_AVAILABLE = True
except ImportError:
    NETWORKX_AVAILABLE = False

try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

# Page configuration
st.set_page_config(
    page_title="Network Visualizer",
    page_icon="🕸️",
    layout="wide"
)

st.title("🕸️ Network Visualizer")
st.write("Create and visualize network graphs showing relationships!")

# Check dependencies
if not NETWORKX_AVAILABLE or not MATPLOTLIB_AVAILABLE:
    st.error("Required libraries not installed. Run:")
    st.code("pip install networkx matplotlib")
    st.stop()

# Initialize session state
if 'edges' not in st.session_state:
    st.session_state['edges'] = []

# --- Sidebar ---
st.sidebar.header("Graph Settings")

graph_type = st.sidebar.selectbox(
    "Graph Type",
    ["Undirected", "Directed"]
)

layout = st.sidebar.selectbox(
    "Layout",
    ["Spring", "Circular", "Kamada-Kawai", "Shell", "Random"]
)

node_size = st.sidebar.slider("Node Size", 100, 3000, 1000)
font_size = st.sidebar.slider("Font Size", 6, 20, 10)
node_color = st.sidebar.color_picker("Node Color", "#6495ED")

# --- Main Interface ---
tab1, tab2, tab3, tab4 = st.tabs(["Add Connections", "View Network", "Analysis", "Export"])

# Tab 1: Add Connections
with tab1:
    st.header("Add Connections")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Add Single Connection")

        with st.form("edge_form"):
            source = st.text_input("From (Source)", placeholder="Alice")
            target = st.text_input("To (Target)", placeholder="Bob")
            weight = st.number_input("Weight (optional)", min_value=0.0, value=1.0)

            if st.form_submit_button("Add Connection"):
                if source and target:
                    st.session_state['edges'].append({
                        'source': source.strip(),
                        'target': target.strip(),
                        'weight': weight
                    })
                    st.success(f"Added: {source} → {target}")
                else:
                    st.error("Please enter both source and target")

    with col2:
        st.subheader("Quick Add Multiple")
        st.write("Enter connections, one per line: `source, target`")

        bulk_input = st.text_area(
            "Connections:",
            placeholder="Alice, Bob\nBob, Charlie\nCharlie, Diana",
            height=150
        )

        if st.button("Add All"):
            lines = bulk_input.strip().split('\n')
            added = 0
            for line in lines:
                if ',' in line:
                    parts = line.split(',')
                    if len(parts) >= 2:
                        st.session_state['edges'].append({
                            'source': parts[0].strip(),
                            'target': parts[1].strip(),
                            'weight': 1.0
                        })
                        added += 1
            if added > 0:
                st.success(f"Added {added} connections!")

    # Upload CSV
    st.subheader("Upload from CSV")
    st.write("CSV should have columns: `source`, `target` (and optionally `weight`)")

    uploaded_file = st.file_uploader("Upload CSV", type=['csv'])

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.dataframe(df.head())

            # Check for required columns
            source_col = None
            target_col = None

            for col in df.columns:
                if col.lower() in ['source', 'from', 'node1']:
                    source_col = col
                if col.lower() in ['target', 'to', 'node2']:
                    target_col = col

            if source_col and target_col:
                if st.button("Import Connections"):
                    weight_col = 'weight' if 'weight' in df.columns else None

                    for idx, row in df.iterrows():
                        st.session_state['edges'].append({
                            'source': str(row[source_col]),
                            'target': str(row[target_col]),
                            'weight': row[weight_col] if weight_col else 1.0
                        })

                    st.success(f"Imported {len(df)} connections!")
            else:
                st.error("Could not find source/target columns")
        except Exception as e:
            st.error(f"Error reading CSV: {e}")

    # Current edges
    st.subheader("Current Connections")

    if st.session_state['edges']:
        df = pd.DataFrame(st.session_state['edges'])
        st.dataframe(df, use_container_width=True)

        if st.button("Clear All"):
            st.session_state['edges'] = []
            st.rerun()
    else:
        st.info("No connections added yet")

# Tab 2: View Network
with tab2:
    st.header("Network Visualization")

    if st.session_state['edges']:
        # Create graph
        if graph_type == "Directed":
            G = nx.DiGraph()
        else:
            G = nx.Graph()

        # Add edges
        for edge in st.session_state['edges']:
            G.add_edge(edge['source'], edge['target'], weight=edge['weight'])

        # Choose layout
        if layout == "Spring":
            pos = nx.spring_layout(G, seed=42)
        elif layout == "Circular":
            pos = nx.circular_layout(G)
        elif layout == "Kamada-Kawai":
            pos = nx.kamada_kawai_layout(G)
        elif layout == "Shell":
            pos = nx.shell_layout(G)
        else:
            pos = nx.random_layout(G, seed=42)

        # Draw network
        fig, ax = plt.subplots(figsize=(12, 8))

        # Get edge weights for width
        weights = [G[u][v]['weight'] for u, v in G.edges()]
        max_weight = max(weights) if weights else 1
        edge_widths = [w / max_weight * 3 + 0.5 for w in weights]

        # Draw edges
        nx.draw_networkx_edges(G, pos, ax=ax, width=edge_widths,
                               alpha=0.6, arrows=(graph_type == "Directed"))

        # Draw nodes
        nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_size,
                               node_color=node_color, alpha=0.9)

        # Draw labels
        nx.draw_networkx_labels(G, pos, ax=ax, font_size=font_size)

        ax.set_title(f"Network Graph ({G.number_of_nodes()} nodes, {G.number_of_edges()} edges)")
        ax.axis('off')

        plt.tight_layout()
        st.pyplot(fig)

        # Store graph for analysis
        st.session_state['graph'] = G

    else:
        st.info("Add connections to see the network visualization")

# Tab 3: Analysis
with tab3:
    st.header("Network Analysis")

    if 'graph' in st.session_state:
        G = st.session_state['graph']

        # Basic stats
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Nodes", G.number_of_nodes())
        with col2:
            st.metric("Edges", G.number_of_edges())
        with col3:
            st.metric("Density", f"{nx.density(G):.3f}")
        with col4:
            if nx.is_connected(G) if not G.is_directed() else nx.is_weakly_connected(G):
                st.metric("Connected", "Yes")
            else:
                st.metric("Connected", "No")

        # Centrality Analysis
        st.subheader("Node Importance (Centrality)")

        centrality_type = st.selectbox(
            "Centrality Measure",
            ["Degree", "Betweenness", "Closeness", "Eigenvector"]
        )

        if centrality_type == "Degree":
            centrality = nx.degree_centrality(G)
            st.caption("Degree centrality: How many connections each node has")
        elif centrality_type == "Betweenness":
            centrality = nx.betweenness_centrality(G)
            st.caption("Betweenness centrality: How often a node appears on shortest paths")
        elif centrality_type == "Closeness":
            centrality = nx.closeness_centrality(G)
            st.caption("Closeness centrality: How close a node is to all others")
        else:
            try:
                centrality = nx.eigenvector_centrality(G, max_iter=500)
            except:
                centrality = nx.degree_centrality(G)
            st.caption("Eigenvector centrality: Connection to other well-connected nodes")

        # Display centrality scores
        centrality_df = pd.DataFrame([
            {'Node': node, 'Centrality': score}
            for node, score in sorted(centrality.items(), key=lambda x: -x[1])
        ])

        col1, col2 = st.columns([1, 2])

        with col1:
            st.dataframe(centrality_df, use_container_width=True)

        with col2:
            # Bar chart
            fig, ax = plt.subplots(figsize=(10, 6))
            top_10 = centrality_df.head(10)
            ax.barh(top_10['Node'], top_10['Centrality'], color='steelblue')
            ax.set_xlabel('Centrality Score')
            ax.set_title(f'Top 10 Nodes by {centrality_type} Centrality')
            ax.invert_yaxis()
            plt.tight_layout()
            st.pyplot(fig)

    else:
        st.info("Create a network first to see analysis")

# Tab 4: Export
with tab4:
    st.header("Export")

    if st.session_state['edges']:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Download Edge List (CSV)")
            df = pd.DataFrame(st.session_state['edges'])
            csv = df.to_csv(index=False)
            st.download_button(
                "Download CSV",
                csv,
                "network_edges.csv",
                "text/csv"
            )

        with col2:
            st.subheader("Download Network Image")

            if 'graph' in st.session_state:
                G = st.session_state['graph']

                # Create figure
                fig, ax = plt.subplots(figsize=(12, 8))

                if layout == "Spring":
                    pos = nx.spring_layout(G, seed=42)
                elif layout == "Circular":
                    pos = nx.circular_layout(G)
                else:
                    pos = nx.kamada_kawai_layout(G)

                nx.draw(G, pos, ax=ax, with_labels=True,
                       node_size=node_size, node_color=node_color,
                       font_size=font_size)

                # Save to buffer
                buf = io.BytesIO()
                fig.savefig(buf, format='png', dpi=150, bbox_inches='tight')
                buf.seek(0)

                st.download_button(
                    "Download PNG",
                    buf,
                    "network.png",
                    "image/png"
                )

                plt.close(fig)
    else:
        st.info("Add connections first to export")

# --- Footer ---
st.markdown("---")
st.markdown("*Built with Streamlit & NetworkX | Digital Scholarship Lab Starter Kit*")
