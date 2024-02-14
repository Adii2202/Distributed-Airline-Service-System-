import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.Map;

// Define the remote interface
public interface AirlineService extends Remote {
    String bookTicket(String passengerName, int flightNumber) throws RemoteException;
    String createFlight(int flightNumber, String destination, int capacity) throws RemoteException;
    String deleteFlight(int flightNumber) throws RemoteException;
    String viewAvailableFlights() throws RemoteException;
    String cancelTicket(String passengerName, int flightNumber) throws RemoteException;
    String getReturnTicketInfo(String passengerName, int flightNumber) throws RemoteException;
    String getPassengerInfo(String passengerName, int flightNumber) throws RemoteException;
    // String getReturnTicketInfo(String passengerName) throws RemoteException;
    Map<String, String> getAllPassengerInfo() throws RemoteException;

}
