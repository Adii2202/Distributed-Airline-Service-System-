import java.rmi.Remote;
import java.rmi.RemoteException;

public interface AirlineService extends Remote {
    String bookTicket(String passengerName, int flightNumber) throws RemoteException;
    String createFlight(int flightNumber, String destination, int capacity) throws RemoteException;
    String deleteFlight(int flightNumber) throws RemoteException;
    String viewAvailableFlights() throws RemoteException;
    String addFlightManually(int flightNumber, String destination, int capacity, int bookedSeats) throws RemoteException;
}
