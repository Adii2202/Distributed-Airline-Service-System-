class Airline:
    def __init__(self, name):
        self.name = name
        self.tickets = {}

    def book_ticket(self, passenger_name, flight_number):
        if flight_number not in self.tickets:
            self.tickets[flight_number] = passenger_name
            return f"Ticket booked for {passenger_name} on flight {flight_number} in Airline '{self.name}'"
        else:
            return f"Ticket already booked for flight {flight_number} in Airline '{self.name}'"

    def cancel_ticket(self, flight_number):
        if flight_number in self.tickets:
            passenger_name = self.tickets.pop(flight_number)
            return f"Ticket canceled for {passenger_name} on flight {flight_number} in Airline '{self.name}'"
        else:
            return f"No booking found for flight {flight_number} in Airline '{self.name}'"

    def get_flight_details(self, flight_number):
        if flight_number in self.tickets:
            passenger_name = self.tickets[flight_number]
            return f"Flight details for flight {flight_number}: Passenger {passenger_name}"
        else:
            return f"No booking found for flight {flight_number} in Airline '{self.name}'"

    def get_all_bookings(self):
        return self.tickets
