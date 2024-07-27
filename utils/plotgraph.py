import networkx as nx
import matplotlib.pyplot as plt

# Read the graph from the GraphML file
G = nx.read_graphml('ernakulam_bus_routes.graphml')

pos = nx.spring_layout(G)  # You can use other layouts if preferred

# Draw nodes as small dots
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=2)  # Small node size

# Draw edges with colors based on route labels
edges = G.edges(data=True)
edge_colors = [data['label'] for _, _, data in edges]  # Use labels as edge colors
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=edge_colors, width=0)

# Remove labels
# Commented out these lines to remove labels
# nx.draw_networkx_labels(G, pos)
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show the plot
plt.title("Graph with Small Nodes and No Labels")
plt.axis('off')  # Hide the axis
plt.show()