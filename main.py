from bus import Bus
import pandas as pd
def process(source,dest):
    station_mapping=pd.read_csv('/home/sivadam/SahaYaatri/cleaned_file.csv')
    if (station_mapping[station_mapping['Station'] == source]['filename'] != station_mapping[station_mapping['Station'] == dest]['filename']):
        return {'bus_routes':[]}
    else:
        filename = station_mapping[station_mapping['Station'] == source]['filename']
        json_path='/home/sivadam/SahaYaatri/JSON_Files'+filename
        graph_path='/home/sivadam/SahaYaatri/JSON_Files'+filename
        busroute = Bus(graph_path,json_path)
        return busroute.process_sd(source,dest)
