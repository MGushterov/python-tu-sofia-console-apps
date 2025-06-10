class TravelAgency():
    def __init__(self, agency_name):
        self.agency_name = agency_name
        self.flights = []


    def add_flight(self, flight):
        self.flights.append(flight)


    def print_all_flights(self):
        print("-------------------------")
        print("-------------------------")
        for flight in self.flights:
            flight_id, destination, price, status = flight.get_id(), flight.get_destination(), flight.get_price(), flight.get_status()
            print(f"ID: {flight_id}, Destination: {destination}, Price: {price:.f2}, Status: {status}")
            print("-------------------------")
            print("-------------------------")
