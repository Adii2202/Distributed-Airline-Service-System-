// import java.rmi.Remote;
// import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
// import java.rmi.server.UnicastRemoteObject;
// import java.util.HashMap;
// import java.util.Map;
// import java.rmi.registry.LocateRegistry;
// import java.rmi.registry.Registry;

public class AirlineServer {
    public static void main(String[] args) {
        try {
            // Create and export the remote object
            AirlineService airlineService = new AirlineServiceImpl();

            // Create a registry on the default port (1098)
            Registry registry = LocateRegistry.createRegistry(1098);

            // Bind the remote object to the registry
            registry.rebind("AirlineService", airlineService);

            System.out.println("AirlineService is ready to accept requests.");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
