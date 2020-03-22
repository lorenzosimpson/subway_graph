from util import Queue

class Station:
    def __init__(self, station_name):
        self.station_name = station_name
    def __repr__(self):
        return f'{self.station_name}'

# create graph class, linking stations
class SubwayGraph:
    def __init__(self):
        self.stations = {}
        self.connections = {}

    def add_station(self, station_name):
        self.stations[station_name] = Station(station_name)
        self.connections[station_name] = set()
    
    def add_connection(self, station_1, station_2):
        if station_1 == station_2:
            print("Error: Can't connect station to itself")
        else:
            self.connections[station_1].add(station_2)
            self.connections[station_2].add(station_1)

    def route(self, origin, destination):
        q = Queue()
        v = set()
        q.enqueue([ origin ])

        while q.size() > 0:
            path = q.dequeue()
            last_node = path[-1]
            if last_node not in v:
                v.add(last_node)

                if last_node == destination:
                    return path, f'{len(path)-2} transfers'
                
                for con in self.connections[last_node]:
                    copy = path.copy()
                    copy.append(con)
                    q.enqueue(copy)

        return 'Sorry, no connection found'

    
# declare locations
locations_upper = [
            'Chambers Street', # 0 connect to times square
            'Union Square', # 1
            'Bedford Avenue', # 2 connect to usq
            '33rd Street', # 3 connect to usq, astor
            'Canal Street', # 4 connect to usq, prince, 
            'Prince Street', # 5 connect to canal st, usq
            'Astor Place', # 6 connect to 33rd Street
            '23rd Street', # 7connect to usq, canal, prince, times
            'Times Square', # 8 connect to usq, 23rd, prince, canal
            'Hudson Yards', # 9 connect to times square
            ]
# initialize subway graph
sg = SubwayGraph()
locations = [l.lower() for l in locations_upper]


# add each station to the graph
for st in locations:
    sg.add_station(st)
# connect the stations to each other
sg.add_connection(locations[1], locations[2])
sg.add_connection(locations[1], locations[3])
sg.add_connection(locations[1], locations[4])
sg.add_connection(locations[1], locations[5])
sg.add_connection(locations[3], locations[6])
sg.add_connection(locations[1], locations[6])
sg.add_connection(locations[1], locations[7])
sg.add_connection(locations[8], locations[1])
sg.add_connection(locations[8], locations[7])
sg.add_connection(locations[8], locations[4])
sg.add_connection(locations[8], locations[5])
sg.add_connection(locations[8], locations[9])
sg.add_connection(locations[4], locations[5])
sg.add_connection(locations[0], locations[8])


print(sg.route(input('Origin: ').lower(), input('Destination: ').lower()))














