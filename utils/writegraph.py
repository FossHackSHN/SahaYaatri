import pandas as pd
import networkx as nx
import os

# Define input and output directories
input_dir = '/Users/sidharthdeepesh/Kerala-Private-Bus-Timing/SahaYaatri/JSON_Files'
output_dir = '/Users/sidharthdeepesh/Kerala-Private-Bus-Timing/SahaYaatri/Graph_Files'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to process a single JSON file and save the graph
def process_json_file(file_path, output_dir):
    # Load the JSON data
    data = pd.read_json(file_path)

    # Create the graph
    G = nx.Graph()

    # Dictionary to store the numerical label of each route
    route_labels = {}

    # Add edges to the graph with numerical labels
    for idx, bus in enumerate(data['busSchedules']):
        route = tuple(bus['route'])
        if route not in route_labels:
            route_labels[route] = idx + 1
        for i in range(len(route) - 1):
            G.add_edge(route[i], route[i + 1], label=route_labels[route], weight=1)

    # Generate output file path
    base_name = os.path.basename(file_path)
    file_name, _ = os.path.splitext(base_name)
    output_file_path = os.path.join(output_dir, f'{file_name}.graphml')

    # Save the graph to GraphML format
    nx.write_graphml(G, output_file_path)

# Process all JSON files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith('.json'):
        file_path = os.path.join(input_dir, file_name)
        process_json_file(file_path, output_dir)

print("Processing complete.")
