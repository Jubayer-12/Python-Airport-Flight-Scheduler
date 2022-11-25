from Travel_Agent import TravelAgent

def main():
    travel_agent = TravelAgent('Go Jaan Travel Agency')
    trip_info1 = travel_agent.set_trip_one_city_one_way('DAC','PRA','10/20/2055')
    # print(trip_info1.aircraft)
    # print(trip_info1.price)
    

    trip_cities = ['DUB','LHR','SYD','JFK']
    trip_info2 = travel_agent.set_trip_multi_city_flexible_route(trip_cities,'16/5/2033')
    
    print('price',trip_info2[1])

    for trip in trip_info2[0]:
        print(trip)


if __name__ == '__main__':
    main()