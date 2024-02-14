import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;

public class AirlineServiceImpl extends UnicastRemoteObject implements AirlineService {
    private Map<Integer, Flight> flights;

    protected AirlineServiceImpl() throws RemoteException {
        super();
        this.flights = new HashMap<>();
        // Add some initial flights for testing
        flights.put(1, new Flight("New York", 100));
        flights.put(2, new Flight("Los Angeles", 150));
    }

    public String bookTicket(String passengerName, int flightNumber) throws RemoteException {
        // Implementation remains the same
        Flight flight = flights.get(flightNumber);
        if (flight != null && flight.bookTicket(passengerName)) {
            return "Ticket booked for " + passengerName + " on Flight " + flightNumber;
        } else {
            return "Unable to book ticket. Please check flight availability.";
        }
    }

    public String createFlight(int flightNumber, String destination, int capacity) throws RemoteException {
        if (!flights.containsKey(flightNumber)) {
            Flight newFlight = new Flight(destination, capacity);
            flights.put(flightNumber, newFlight);
            return "Flight " + flightNumber + " to " + destination + " created with capacity " + capacity;
        } else {
            return "Flight " + flightNumber + " already exists. Choose a different flight number.";
        }
    }

    public String deleteFlight(int flightNumber) throws RemoteException {
        if (flights.containsKey(flightNumber)) {
            flights.remove(flightNumber);
            return "Flight " + flightNumber + " deleted successfully.";
        } else {
            return "Flight " + flightNumber + " does not exist.";
        }
    }

    public String viewAvailableFlights() throws RemoteException {
        StringBuilder result = new StringBuilder("Available Flights:\n");
        for (Map.Entry<Integer, Flight> entry : flights.entrySet()) {
            result.append("Flight ").append(entry.getKey()).append(": ")
                    .append(entry.getValue().getDestination()).append(", Available Seats: ")
                    .append(entry.getValue().getAvailableSeats()).append("\n");
        }
        return result.toString();
    }

    public String addFlightManually(int flightNumber, String destination, int capacity, int bookedSeats) throws RemoteException {
        if (!flights.containsKey(flightNumber)) {
            Flight newFlight = new Flight(destination, capacity, bookedSeats);
            flights.put(flightNumber, newFlight);
            return "Manually added Flight " + flightNumber + " to " + destination + " with capacity " + capacity +
                    " and booked seats " + bookedSeats;
        } else {
            return "Flight " + flightNumber + " already exists. Choose a different flight number.";
        }
    }

    // Inner class representing a Flight
    private static class Flight {
        private String destination;
        private int capacity;
        private int bookedSeats;

        public Flight(String destination, int capacity) {
            this.destination = destination;
            this.capacity = capacity;
            this.bookedSeats = 0;
        }

        public Flight(String destination, int capacity, int bookedSeats) {
            this.destination = destination;
            this.capacity = capacity;
            this.bookedSeats = bookedSeats;
        }

        public String getDestination() {
            return destination;
        }

        public int getAvailableSeats() {
            return capacity - bookedSeats;
        }

        public boolean bookTicket(String passengerName) {
            if (bookedSeats < capacity) {
                bookedSeats++;
                return true;
            } else {
                return false;
            }
        }
    }
}
