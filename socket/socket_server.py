import socket

# Define host and port
HOST = '127.0.0.1'  # localhost
PORT = 12345        # Arbitrary non-privileged port

# Sample flight data
flights = {
    '1': {'name': 'Flight 1', 'status': 'Available', 'seats': 100, 'schedule': '09:00 AM'},
    '2': {'name': 'Flight 2', 'status': 'Available', 'seats': 150, 'schedule': '12:00 PM'},
    '3': {'name': 'Flight 3', 'status': 'Available', 'seats': 120, 'schedule': '03:00 PM'},
}

# Function to book a flight
def book_flight(flight_id):
    if flight_id in flights and flights[flight_id]['status'] == 'Available':
        flights[flight_id]['status'] = 'Booked'
        flights[flight_id]['seats'] -= 1
        return 'Booking successful!'
    else:
        return 'Invalid flight ID or flight not available.'

# Function to list available flights
def list_available_flights():
    available_flights = [f"{key}: {flight['name']} ({flight['schedule']})" for key, flight in flights.items() if flight['status'] == 'Available']
    return '\n'.join(available_flights) if available_flights else 'No available flights.'

# Function to display the flight schedule
def display_flight_schedule():
    flight_schedule = [f"{key}: {flight['name']} - {flight['schedule']}" for key, flight in flights.items()]
    return '\n'.join(flight_schedule)

# Function to view flight details
def view_flight_details(flight_id):
    if flight_id in flights:
        flight = flights[flight_id]
        details = f"Flight: {flight['name']}\nStatus: {flight['status']}\nSeats available: {flight['seats']}\nSchedule: {flight['schedule']}"
        return details
    else:
        return 'Invalid flight ID.'

# Function to cancel flight booking
def cancel_flight_booking(flight_id):
    if flight_id in flights and flights[flight_id]['status'] == 'Booked':
        flights[flight_id]['status'] = 'Available'
        flights[flight_id]['seats'] += 1
        return 'Flight booking canceled successfully!'
    else:
        return 'Invalid flight ID or flight not booked.'

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the address
    server_socket.bind((HOST, PORT))
    # Listen for incoming connections
    server_socket.listen()

    print('Server is listening...')

    while True:
        # Accept connections from client
        conn, addr = server_socket.accept()
        with conn:
            print('Connected by', addr)
            while True:
                # Receive data from client
                data = conn.recv(1024)
                if not data:
                    break
                command = data.decode()
                # Process command
                if command.startswith('book'):
                    _, flight_id = command.split()
                    response = book_flight(flight_id)
                elif command.startswith('available'):
                    response = list_available_flights()
                elif command.startswith('schedule'):
                    response = display_flight_schedule()
                elif command.startswith('view'):
                    _, flight_id = command.split()
                    response = view_flight_details(flight_id)
                elif command.startswith('cancel'):
                    _, flight_id = command.split()
                    response = cancel_flight_booking(flight_id)
                else:
                    response = 'Invalid command.'
                # Send response to client
                conn.sendall(response.encode())
