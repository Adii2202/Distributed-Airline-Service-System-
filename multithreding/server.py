from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
import threading
import string
import random
from datetime import datetime
from prettytable import PrettyTable

# Model classes
class User:
    def __init__(self, username):
        self.username = username
        self.history = []
        self.curr_flight = None

    def __str__(self):
        return f"['username': {self.username}, 'history': {self.history}, 'curr_flight': {self.curr_flight}]"

    def addToSeen(self, f):
        self.history.append({"flight": f.flight_number, "status": "seen"})
        self.curr_flight = f

    def bookFlightThread(self, flight_class):
        print("User thread running...")
        self.history[-1]["status"] = "booked"

    def bookFlight(self, flight_class):
        thread = threading.Thread(target=self.bookFlightThread, args=(flight_class,))
        thread.start()

class Flight:
    def __init__(self, flight_number, source, destination, time_of_flight, no_of_seats, available_economy_seats, economy_price, business_price, airline):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.time_of_flight = time_of_flight
        self.no_of_seats = no_of_seats
        self.available_economy_seats = available_economy_seats
        self.available_business_seats = self.no_of_seats - self.available_economy_seats
        self.available_seats = no_of_seats
        self.economy_price = economy_price
        self.business_price = business_price
        self.airline = airline

    def fillASeatThread(self, flight_class):
        print("Flight thread running...")
        if flight_class == "E":
            self.available_economy_seats -= 1
        else:
            self.available_business_seats -= 1
        self.available_seats = self.available_economy_seats + self.available_business_seats

    def fillASeat(self, flight_class):
        thread = threading.Thread(target=self.fillASeatThread, args=(flight_class,))
        thread.start()

    def __str__(self):
        return f"['flight_number': {self.flight_number}, 'source': {self.source}, 'destination': {self.destination}, 'time_of_flight': {self.time_of_flight}, 'no_of_seats': {self.no_of_seats}, 'available_economy_seats': {self.available_economy_seats}, 'economy_price': {self.economy_price}, 'business_price': {self.business_price}, 'airline': {self.airline}]"

# Static Data
airlines = [
    {"name": "British Airways", "cost_b": random.randint(1000, 2000), "cost_e": random.randint(100, 200)},
    {"name": "Air India", "cost_b": random.randint(1000, 2000), "cost_e": random.randint(100, 200)},
    {"name": "SpiceJet", "cost_b": random.randint(1000, 2000), "cost_e": random.randint(100, 200)},
    {"name": "Jet Airways", "cost_b": random.randint(1000, 2000), "cost_e": random.randint(100, 200)},
]
cities = ["Mumbai", "Pune", "New Delhi", "Bangalore", "Chennai", "Kolkata"]
times = [
    datetime.strptime("13 Sep 2023", "%d %b %Y").replace(hour=9, minute=0),
    datetime.strptime("15 Sep 2023", "%d %b %Y").replace(hour=12, minute=0),
    datetime.strptime("16 Nov 2023", "%d %b %Y").replace(hour=15, minute=0),
    datetime.strptime("13 Oct 2023", "%d %b %Y").replace(hour=18, minute=0),
    datetime.strptime("28 Sep 2023", "%d %b %Y").replace(hour=21, minute=0),
]
flights = []
user = User("admin")
for i in range(4):
    c = random.sample(cities, 2)
    airline = random.choice(airlines)
    flights.append(
        Flight(
            flight_number="".join(random.choices(string.ascii_letters + string.digits, k=6)),
            source=c[0],
            destination=c[1],
            time_of_flight=random.choice(times),
            no_of_seats=random.randint(200, 300),
            available_economy_seats=random.randint(150, 200),
            economy_price=airline["cost_e"],
            business_price=airline["cost_b"],
            airline=airline["name"],
        )
    )

# Server connection

def get_flights():
    return flights

def view_flights():
    table = PrettyTable(
        [
            "flight_ID",
            "src",
            "dest",
            "time_of_flight",
            "available_seats",
            "available_e_seats",
            "available_b_seats",
            "e_price",
            "b_price",
            "airline",
        ]
    )
    table.title = "Flights"
    for i in range(len(flights)):
        f = flights[i]
        table.add_row(
            [
                f.flight_number,
                f.source,
                f.destination,
                f.time_of_flight,
                f.available_seats,
                f.available_economy_seats,
                f.available_business_seats,
                f.economy_price,
                f.business_price,
                f.airline,
            ]
        )
    return table.get_string()

def bookFlight(id, flight_class):
    for f in flights:
        if f.flight_number == id:
            user.addToSeen(f)
            break
    if flight_class == "B":
        return user.curr_flight.business_price
    else:
        return user.curr_flight.economy_price

def pay(flight_class):
    user.bookFlight(flight_class)
    user.curr_flight.fillASeat(flight_class)

class SimpleThreadedXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

server_addr = ("localhost", 3000)
server = SimpleXMLRPCServer(("localhost", 3000), allow_none=True)
server.register_function(get_flights)
server.register_function(pay)
server.register_function(bookFlight)
server.register_function(view_flights)

if __name__ == "__main__":
    try:
        print("Server thread started. Testing server ...")
        print('listening on localhost port 3000')
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")
