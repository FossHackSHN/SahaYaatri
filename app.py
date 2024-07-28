from flask import Flask, request, jsonify
from bus import Bus
import pandas as pd

app = Flask(__name__)

def process(source, dest):
    station_mapping = pd.read_csv('./cleaned_file.csv')
    source_file = station_mapping[station_mapping['Station'] == source]['Filename'].values[0]
    dest_file = station_mapping[station_mapping['Station'] == dest]['Filename'].values[0]
    
    if source_file != dest_file:
        return {'bus_routes': []}
    else:
        filename = source_file
        json_path = './JSON_Files/' + filename
        graph_path = './Graph_Files/' + filename[:-5]+'.graphml'
        print
        busroute = Bus(graph_path, json_path)
        return busroute.process_sd(source, dest)

@app.route('/bus_routes', methods=['POST'])
def get_route():
    data = request.json
    source = data.get('source')
    destination = data.get('destination')
    
    if not source or not destination:
        return jsonify({'error': 'Please provide both source and destination'}), 400
    
    result = process(source, destination)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
