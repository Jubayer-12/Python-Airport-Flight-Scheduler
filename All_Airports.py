import csv
from Airport import Airport
from math import radians,sin,cos,atan2,sqrt


class AllAirports:

    def __init__(self) -> None:
        self.airports = None
        self.load_allAirports_data('airport.csv')

    def load_allAirports_data(self,airport_file):
        store_airports = {}
        currency_rate = {}
        country_currency = {}


        #get currency name <---> rate
        with open('currencyrates.csv','r') as currency_rates_file:
            lines = csv.reader(currency_rates_file)

            for line in lines:
                currency_rate[line[1]] = line[2]

        currency_rates_file.close()


        #get country  <---> currency name 
        with open('countrycurrency.csv','r') as country_currency_file:
            lines = csv.reader(country_currency_file)
            next(lines)

            for line in lines:
                country_currency[line[0]] = line[1]

        country_currency_file.close()


        #Create Airport
        with open(airport_file,'r',encoding="utf-8") as file:
            lines = csv.reader(file)

            try:
                for line in lines:
                    country_name = line[3]
                    if country_name not in country_currency:
                        continue
                    currency_name = country_currency[country_name]
                    if currency_name not in currency_rate:
                        continue
                    rate = currency_rate[currency_name]
                    
                    store_airports[line[4]] = Airport(line[4],line[1],line[2],line[3],line[6],line[7],rate)

            except KeyError as e:
                print(e)

            self.airports = store_airports



        file.close()

    
    def get_distance_between_two_airports(self, lat1, lon1, lat2, lon2):
        radius = 6371
        lat_diff = radians(lat1 - lat2)
        lon_diff = radians(lon1 - lon2)
        a = (sin(lat_diff / 2) * sin(lat_diff / 2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(lon_diff / 2) * sin(lon_diff / 2))
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = radius * c
        return distance

    def distance_between_two_airports(self,airport1_code,airport2_code):

        airport1 = self.airports[airport1_code]
        airport2 = self.airports[airport2_code]
        distance = self.get_distance_between_two_airports(airport1.lat,airport1.lon,airport2.lat,airport2.lon)
        return distance

    def get_ticket_price(self,start,end):
        distance = self.distance_between_two_airports(start,end)
        airport1 = self.airports[start]
        fare = distance * airport1.rate
        return fare




world_tour = AllAirports()

fare = world_tour.get_ticket_price('DAC','PRA')
print('Ticket Fare:',fare)