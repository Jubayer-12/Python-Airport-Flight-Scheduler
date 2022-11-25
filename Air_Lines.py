import csv
from Aircraft import Aircraft

class AirLines:
    def __init__(self) -> None:
        self.aircraft = None
        self.load_AirCraft_data('aircraft.csv')


    def load_AirCraft_data(self,aircraft_file):

        AirCrafts = {}

        with open(aircraft_file,'r') as air_craft_file:
            lines = csv.reader(air_craft_file)
            next(lines)

            for line in lines:
                AirCrafts[line[0]] = Aircraft(line[3],line[0],line[1],line[4])

        air_craft_file.close()


        self.aircraft = AirCrafts


    def get_aircraft(self,aircraft_code):
        return self.aircraft[aircraft_code]

    def get_aircraft_by_distance(self,distance):
        for aircraft in self.aircraft.values():
            if aircraft.flight_range < distance:
                return aircraft






AirLines()