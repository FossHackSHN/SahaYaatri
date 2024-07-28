import os
import pandas as pd
import json

def process_json_files(folder_path):
    # Dictionary to hold station names and the corresponding file names
    stations_dict = {}

    # Loop through each file in the directory
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            
            # Load JSON data from file
            with open(file_path, 'r') as file:
                data = json.load(file)
                data=data.get('busSchedules')
                
                for d in data:
                    route_stations = d.get('route', [])
                    schedule_stations = [station['station'] for trip in d.get('schedule', []) for station in trip.get('stations', [])]

                    # Combine all stations
                    all_stations = set(route_stations + schedule_stations)
                    
                    # Add stations to dictionary
                    for station in all_stations:
                        if station not in stations_dict:
                            stations_dict[station] = []
                        stations_dict[station].append(filename)

    # Convert dictionary to DataFrame
    records = []
    for station, files in stations_dict.items():
        for file in files:
            records.append({'Station': station, 'Filename': file})

    df = pd.DataFrame(records)

    # Save DataFrame to CSV
    df.to_csv('stations_mapping.csv', index=False)
    print("CSV file 'stations_mapping.csv' created successfully.")

# Define the path to the folder containing JSON files
folder_path = '/home/sivadam/SahaYaatri/JSON_Files'
process_json_files(folder_path)
