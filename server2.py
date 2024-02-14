import Pyro4
import pymongo

@Pyro4.expose
class AirlineServiceInterface:
    def __init__(self):
        self.airline_database = AirlineDatabase()

    def create_airline(self, airline_name):
        return self.airline_database.add_airline(airline_name)

    def get_airline_names(self):
        return self.airline_database.get_airline_names()

    def execute_airline_function(self, airline_name, function_name, *args):
        if airline_name in self.airline_database.get_airline_names():
            return getattr(self.airline_database, function_name)(airline_name, *args)
        else:
            return f"Airline '{airline_name}' not found"


class AirlineDatabase:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["airline_database"]
        self.airlines_collection = self.db["airlines"]

    def add_airline(self, name):
        if self.airlines_collection.find_one({"name": name}):
            return f"Airline '{name}' already exists."
        
        airline_data = {"name": name, "flights": []}
        result = self.airlines_collection.insert_one(airline_data)
        
        if result.inserted_id:
            return f"Airline '{name}' added successfully."
        else:
            return f"Failed to add airline '{name}'."

    def get_airline_names(self):
        return [airline["name"] for airline in self.airlines_collection.find()]

    def book_ticket(self, airline_name, flight_number, passenger_name):
        # Add a ticket to the specified flight of the airline
        result = self.airlines_collection.update_one(
            {"name": airline_name, "flights": flight_number},
            {"$addToSet": {"flights.$[elem].tickets": passenger_name}},
            array_filters=[{"elem.flight_number": flight_number}]
        )
        if result.modified_count > 0:
            return f"Ticket booked for {passenger_name} on flight {flight_number} in Airline '{airline_name}'."
        else:
            return f"Failed to book ticket for {passenger_name} on flight {flight_number} in Airline '{airline_name}'."

    def cancel_ticket(self, airline_name, flight_number, passenger_name):
        # Cancel a ticket for the specified flight of the airline
        result = self.airlines_collection.update_one(
            {"name": airline_name, "flights": flight_number},
            {"$pull": {"flights.$[elem].tickets": passenger_name}},
            array_filters=[{"elem.flight_number": flight_number}]
        )
        if result.modified_count > 0:
            return f"Ticket canceled for {passenger_name} on flight {flight_number} in Airline '{airline_name}'."
        else:
            return f"No booking found for {passenger_name} on flight {flight_number} in Airline '{airline_name}'."

    def get_flight_details(self, airline_name, flight_number):
        airline = self.airlines_collection.find_one({"name": airline_name, "flights": flight_number})
        if airline:
            tickets = airline.get("flights", [])[0].get("tickets", [])
            return f"Details for flight {flight_number} in Airline '{airline_name}': Passengers {', '.join(tickets)}"
        else:
            return f"No booking found for flight {flight_number} in Airline '{airline_name}'."

    def get_all_bookings(self, airline_name):
        airline = self.airlines_collection.find_one({"name": airline_name})
        if airline:
            all_bookings = {}
            for flight in airline.get("flights", []):
                all_bookings[flight["flight_number"]] = flight.get("tickets", [])
            return all_bookings
        else:
            return {}

def main():
    airline_service = AirlineServiceInterface()
    with Pyro4.Daemon() as daemon:
        uri = daemon.register(airline_service)
        print("AirlineServiceServer is ready. URI:", uri)
        daemon.requestLoop()

if __name__ == "__main__":
    main()
