import pymongo

class AirlineDatabase:
    def __init__(self):
        # Connect to MongoDB (Make sure MongoDB is running locally or provide the connection URI)
        self.client = pymongo.MongoClient("mongodb://localhost:27017")
        # Create or get the database (replace 'airline_database' with your desired database name)
        self.db = self.client["airline_database"]
        # Create or get the collection (replace 'airlines' with your desired collection name)
        self.airlines_collection = self.db["airlines"]

    def add_airline(self, name):
        # Check if the airline already exists
        if self.airlines_collection.find_one({"name": name}):
            return f"Airline '{name}' already exists."
        
        # Insert the airline details into the collection
        airline_data = {"name": name, "flights": []}
        result = self.airlines_collection.insert_one(airline_data)
        
        if result.inserted_id:
            return f"Airline '{name}' added successfully."
        else:
            return f"Failed to add airline '{name}'."

    def get_airline_names(self):
        # Return a list of all airline names
        return [airline["name"] for airline in self.airlines_collection.find()]

    def add_flight(self, airline_name, flight_number):
        # Add a flight to the specified airline
        result = self.airlines_collection.update_one(
            {"name": airline_name},
            {"$addToSet": {"flights": flight_number}}
        )
        if result.modified_count > 0:
            return f"Flight {flight_number} added to Airline '{airline_name}'."
        else:
            return f"Failed to add flight {flight_number} to Airline '{airline_name}'."

    def get_flights(self, airline_name):
        # Return a list of flights for the specified airline
        airline = self.airlines_collection.find_one({"name": airline_name})
        if airline:
            return airline.get("flights", [])
        else:
            return []

# Example Usage
if __name__ == "__main__":
    db = AirlineDatabase()

    # Add Airlines
    print(db.add_airline("Airline1"))
    print(db.add_airline("Airline2"))

    # Get Airline Names
    print("Airline Names:", db.get_airline_names())

    # Add Flights
    print(db.add_flight("Airline1", "FL123"))
    print(db.add_flight("Airline1", "FL456"))
    print(db.add_flight("Airline2", "FL789"))

    # Get Flights for an Airline
    print("Flights for Airline1:", db.get_flights("Airline1"))
    print("Flights for Airline2:", db.get_flights("Airline2"))
