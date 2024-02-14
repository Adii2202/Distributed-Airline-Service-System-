import Pyro4

@Pyro4.expose
class AirlineClient:
    def __init__(self, server_uri):
        self.airline_service = Pyro4.Proxy(server_uri)

    def create_airline(self, airline_name):
        return self.airline_service.create_airline(airline_name)

    def get_airline_names(self):
        return self.airline_service.get_airline_names()

    def execute_airline_function(self, airline_name, function_name, *args):
        return self.airline_service.execute_airline_function(airline_name, function_name, *args)


def main():
    # Replace this URI with the actual URI printed by the server
    server_uri = "PYRO:obj_49d397a468f54e39a1ab61cc63832116@localhost:58053"

    airline_client = AirlineClient(server_uri)

    try:
        airline_name = input("Enter the name of the airline: ")
        print(airline_client.create_airline(airline_name))

        while True:
            print("\nAvailable functions:")
            print("1. book_ticket")
            print("2. cancel_ticket")
            print("3. get_flight_details")
            print("4. get_all_bookings")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "5":
                break

            function_name = ""
            passenger_name = ""
            flight_number = ""

            if choice == "1":
                function_name = "book_ticket"
                passenger_name = input("Enter passenger name: ")
                flight_number = input("Enter flight number: ")
            elif choice == "2":
                function_name = "cancel_ticket"
                flight_number = input("Enter flight number: ")
            elif choice == "3":
                function_name = "get_flight_details"
                flight_number = input("Enter flight number: ")
            elif choice == "4":
                function_name = "get_all_bookings"
            
            if function_name:
                result = airline_client.execute_airline_function(airline_name, function_name, passenger_name, flight_number)
                print(result)
            else:
                print("Invalid choice. Please enter a valid option.")

    except Pyro4.errors.CommunicationError as e:
        print("Error connecting to the Pyro server:", e)

if __name__ == "__main__":
    main()
