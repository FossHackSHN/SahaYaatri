import networkx as nx
import matplotlib.pyplot as plt

# Read the graph from the GraphML file
G = nx.read_graphml('/Users/sidharthdeepesh/Kerala-Private-Bus-Timing/SahaYaatri/Graph_Files/ernakulam.graphml')

def get_route_segments(G, source, target):
    try:
        path = nx.shortest_path(G, source=source, target=target, weight='weight')
        route_segments = {}
        
        # Iterate through the path to extract labels and segments
        for i in range(len(path) - 1):
            start = path[i]
            end = path[i + 1]
            label = G[start][end]['label']
            
            if label not in route_segments:
                route_segments[label] = []
                
            route_segments[label].append((start, end))
        
        return route_segments
    except nx.NetworkXNoPath:
        return f"No path exists between {source} and {target}"