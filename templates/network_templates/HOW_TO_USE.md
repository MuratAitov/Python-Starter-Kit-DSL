# 🕸️ Network Analysis Templates

Visualize relationships and connections in your data.

## What You Can Build

- **Social networks** — Visualize connections between people
- **Citation networks** — Show how papers reference each other
- **Organizational charts** — Display hierarchies
- **Concept maps** — Connect related ideas
- **Influence diagrams** — Show who influences whom

---

## Available Templates

### 1. `simple_network.py` — Network Visualizer (Streamlit App)
An interactive web app to create and visualize networks.

**Features:**
- Add nodes and edges manually
- Upload network data from CSV
- Interactive visualization
- Export network image

**How to use:**

1. **Run the app:**
   ```bash
   streamlit run templates/network_templates/simple_network.py
   ```

2. **Add connections** between entities

3. **Visualize** the network

---

### 2. `network_analysis.py` — Network Analysis Script
A script for analyzing network properties.

**Features:**
- Calculate network statistics
- Find central nodes
- Detect communities
- Export results

**How to use:**

1. **Prepare your data** as edge list (CSV with source, target columns)

2. **Run the script:**
   ```bash
   python templates/network_templates/network_analysis.py
   ```

---

## Example Ideas

### Simple Ideas (Beginners)
- **Friend Network** — Who knows who in a group
- **Character Map** — Connections in a book/movie
- **Team Collaboration** — Who works with whom
- **Family Tree** — Family relationships

### Medium Ideas
- **Citation Analysis** — How research papers connect
- **Email Network** — Communication patterns
- **Hashtag Network** — Related hashtags on social media
- **Collaboration Network** — Co-authorship patterns

### Advanced Ideas
- **Influence Analysis** — Find key influencers
- **Community Detection** — Find groups in networks
- **Temporal Networks** — How connections change over time
- **Bipartite Networks** — Two types of nodes (e.g., people & events)

---

## Quick Tips

### Create a Simple Network
```python
import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(['Alice', 'Bob', 'Charlie', 'Diana'])

# Add edges (connections)
G.add_edge('Alice', 'Bob')
G.add_edge('Bob', 'Charlie')
G.add_edge('Charlie', 'Diana')
G.add_edge('Alice', 'Diana')

# Draw
nx.draw(G, with_labels=True, node_color='lightblue',
        node_size=1000, font_size=12)
plt.show()
```

### Create from Edge List
```python
import networkx as nx
import pandas as pd

# Load edges from CSV
# CSV should have columns: source, target
edges = pd.read_csv('edges.csv')

# Create graph from edges
G = nx.from_pandas_edgelist(edges, 'source', 'target')

# Draw
nx.draw(G, with_labels=True)
plt.show()
```

### Add Node Attributes
```python
# Add attributes when creating nodes
G.add_node('Alice', role='Manager', department='Sales')
G.add_node('Bob', role='Developer', department='Engineering')

# Access attributes
print(G.nodes['Alice']['role'])  # 'Manager'

# Color by attribute
colors = ['red' if G.nodes[n].get('department') == 'Sales' else 'blue'
          for n in G.nodes()]
nx.draw(G, node_color=colors, with_labels=True)
```

### Add Edge Weights
```python
# Weighted edges (e.g., strength of connection)
G.add_edge('Alice', 'Bob', weight=5)
G.add_edge('Bob', 'Charlie', weight=2)

# Draw with edge width based on weight
edges = G.edges()
weights = [G[u][v]['weight'] for u, v in edges]
nx.draw(G, with_labels=True, width=weights)
```

### Network Statistics
```python
# Basic stats
print(f"Nodes: {G.number_of_nodes()}")
print(f"Edges: {G.number_of_edges()}")
print(f"Density: {nx.density(G):.3f}")

# Centrality (who's most connected/important)
centrality = nx.degree_centrality(G)
for node, score in sorted(centrality.items(), key=lambda x: -x[1]):
    print(f"{node}: {score:.3f}")

# Most connected node
most_connected = max(centrality, key=centrality.get)
print(f"Most central: {most_connected}")
```

### Directed Networks
```python
# For relationships with direction (A -> B)
G = nx.DiGraph()

G.add_edge('A', 'B')  # A points to B
G.add_edge('B', 'C')
G.add_edge('A', 'C')

# Draw with arrows
nx.draw(G, with_labels=True, arrows=True,
        connectionstyle='arc3,rad=0.1')
```

### Better Layouts
```python
# Different layout algorithms
pos = nx.spring_layout(G)      # Force-directed (default)
pos = nx.circular_layout(G)    # Circle
pos = nx.kamada_kawai_layout(G)  # Alternative force-directed
pos = nx.shell_layout(G)       # Concentric circles

nx.draw(G, pos=pos, with_labels=True)
```

### Interactive Visualization
```python
# Using pyvis for interactive HTML graphs
from pyvis.network import Network

net = Network(notebook=True, height='500px', width='100%')

# Add nodes and edges
net.add_node('Alice')
net.add_node('Bob')
net.add_edge('Alice', 'Bob')

# Show
net.show('network.html')
```

---

## Common Issues

### "Module not found: networkx"
```bash
pip install networkx
```

### "Module not found: pyvis"
```bash
pip install pyvis
```

### Graph looks messy
```python
# Try different layouts
pos = nx.kamada_kawai_layout(G)
nx.draw(G, pos=pos, with_labels=True)

# Or adjust figure size
plt.figure(figsize=(12, 8))
nx.draw(G, with_labels=True)
```

### Labels overlap
```python
# Reduce label size or adjust positions
nx.draw(G, with_labels=True, font_size=8)

# Or use node IDs and show labels separately
pos = nx.spring_layout(G)
nx.draw(G, pos)
nx.draw_networkx_labels(G, pos, font_size=8)
```

### Too many nodes
```python
# Filter to show only important nodes
# Example: nodes with degree > 5
important = [n for n in G.nodes() if G.degree(n) > 5]
subgraph = G.subgraph(important)
nx.draw(subgraph, with_labels=True)
```

---

## Learn More

- [NetworkX Documentation](https://networkx.org/documentation/stable/)
- [NetworkX Tutorial](https://networkx.org/documentation/stable/tutorial.html)
- [PyVis Documentation](https://pyvis.readthedocs.io/)
- [Network Analysis with Python](https://programminghistorian.org/en/lessons/exploring-and-analyzing-network-data-with-python)

---

**Need help?** Ask your instructor or check the main README.md
