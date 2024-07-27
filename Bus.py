import pandas as pd
from datetime import datetime, timedelta
import networkx as nx
import os


class Bus():
    def __init__(self,graph_path,json_path):
        self.G = nx.read_graphml(graph_path)
        self.bus_data=pd.read_json(json_path)
    def parse_time(self,time_str):
        return datetime.strptime(time_str, '%I:%M %p')

    def get_direct_route_buses(self,source, destination):
        routes = []
        for bus in self.bus_data['busSchedules']:
            for trip in bus["schedule"]:
                source_time = None
                dest_time = None
                for station in trip["stations"]:
                    if station["station"] == source:
                        source_time = self.parse_time(station["departureTime"])
                    if station["station"] == destination:
                        dest_time = self.parse_time(station["arrivalTime"])
                    if source_time and dest_time and dest_time > source_time:
                        routes.append({
                            "Vehicle Number": bus["Vehicle Number"],
                            "trip": trip["trip"],
                            "source_departure": source_time.strftime('%I:%M %p'),
                            "destination_arrival": dest_time.strftime('%I:%M %p'),
                            "duration": str(dest_time - source_time)
                        })
                        break
        
        return routes

    def get_route_segments(self,source,target):
        try:
            path = nx.shortest_path(self.G, source=source, target=target, weight='weight')
            route_segments = {}
            
            # Iterate through the path to extract labels and segments
            for i in range(len(path) - 1):
                start = path[i]
                end = path[i + 1]
                label = self.G[start][end]['label']
                
                if label not in route_segments:
                    route_segments[label] = []
                    
                route_segments[label].append((start, end))
            
            return route_segments
        except nx.NetworkXNoPath:
            return -1
        
    def process(self,source,dest):
        route_segments= self.get_route_segments(source,dest)
        routes=[]
        result={}
        for i in route_segments.items():
            routes.append(self.get_direct_route_buses(i[0][0],i[-1][1]))
        result['bus_routes']=routes
        return result
