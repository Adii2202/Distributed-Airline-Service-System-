// import java.rmi.RemoteException;
// import java.rmi.registry.LocateRegistry;
// import java.rmi.registry.Registry;
// import java.util.Scanner;

// public class AirlineServer {
//     public static void main(String[] args) {
//         try {
//             // Create and export the remote object
//             AirlineService airlineService = new AirlineServiceImpl();

//             // Create a registry on the default port (1098)
//             Registry registry = LocateRegistry.createRegistry(1098);

//             // Bind the remote object to the registry
//             registry.rebind("AirlineService", airlineService);

//             System.out.println("AirlineService is ready to accept requests.");

//             // Interactive menu for server operations
//             Scanner scanner = new Scanner(System.in);
//             while (true) {
//                 System.out.println("\n=== Server Options ===");
//                 System.out.println("1. Create Flight");
//                 System.out.println("2. Delete Flight");
//                 System.out.println("0. Exit");

//                 System.out.print("Enter your choice: ");
//                 int choice = scanner.nextInt();

//                 switch (choice) {
//                     case 1:
//                         createFlight(airlineService, scanner);
//                         break;
//                     case 2:
//                         deleteFlight(airlineService, scanner);
//                         break;
//                     case 0:
//                         System.out.println("Exiting Server.");
//                         System.exit(0);
//                         break;
//                     default:
//                         System.out.println("Invalid choice. Please try again.");
//                 }
//             }

//         } catch (Exception e) {
//             e.printStackTrace();
//         }
//     }

//     private static void createFlight(AirlineService airlineService, Scanner scanner) {
//         try {
//             System.out.print("Enter flight number: ");
//             int flightNumber = readIntegerInput(scanner);
    
//             System.out.print("Enter destination: ");
//             String destination = scanner.next();
    
//             System.out.print("Enter capacity: ");
//             int capacity = readIntegerInput(scanner);
    
//             String result = airlineService.createFlight(flightNumber, destination, capacity);
//             System.out.println(result);
    
//         } catch (RemoteException e) {
//             e.printStackTrace();
//         }
//     }
    
//     private static int readIntegerInput(Scanner scanner) {
//         while (!scanner.hasNextInt()) {
//             System.out.println("Invalid input. Please enter a valid integer.");
//             scanner.next(); // Consume the invalid input
//         }
//         return scanner.nextInt();
//     }
    

//     private static void deleteFlight(AirlineService airlineService, Scanner scanner) {
//         try {
//             System.out.print("Enter flight number to delete: ");
//             int flightNumber = scanner.nextInt();

//             String result = airlineService.deleteFlight(flightNumber);
//             System.out.println(result);

//         } catch (RemoteException e) {
//             e.printStackTrace();
//         }
//     }
// }



import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Map;
import java.util.Scanner;

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

            // Interactive menu for server operations
            Scanner scanner = new Scanner(System.in);
            while (true) {
                System.out.println("\n=== Server Options ===");
                System.out.println("1. Create Flight");
                System.out.println("2. Delete Flight");
                System.out.println("3. View All Passenger Info");
                System.out.println("0. Exit");

                System.out.print("Enter your choice: ");
                int choice = scanner.nextInt();

                switch (choice) {
                    case 1:
                        createFlight(airlineService, scanner);
                        break;
                    case 2:
                        deleteFlight(airlineService, scanner);
                        break;
                    case 3:
                        viewAllPassengerInfo(airlineService);
                        break;
                    case 0:
                        System.out.println("Exiting Server.");
                        System.exit(0);
                        break;
                    default:
                        System.out.println("Invalid choice. Please try again.");
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void createFlight(AirlineService airlineService, Scanner scanner) {
        try {
            System.out.print("Enter flight number: ");
            int flightNumber = readIntegerInput(scanner);

            System.out.print("Enter destination: ");
            String destination = scanner.next();

            System.out.print("Enter capacity: ");
            int capacity = readIntegerInput(scanner);

            String result = airlineService.createFlight(flightNumber, destination, capacity);
            System.out.println(result);

        } catch (RemoteException e) {
            e.printStackTrace();
        }
    }

    private static int readIntegerInput(Scanner scanner) {
        while (!scanner.hasNextInt()) {
            System.out.println("Invalid input. Please enter a valid integer.");
            scanner.next(); // Consume the invalid input
        }
        return scanner.nextInt();
    }

    private static void deleteFlight(AirlineService airlineService, Scanner scanner) {
        try {
            System.out.print("Enter flight number to delete: ");
            int flightNumber = scanner.nextInt();

            String result = airlineService.deleteFlight(flightNumber);
            System.out.println(result);

        } catch (RemoteException e) {
            e.printStackTrace();
        }
    }

    private static void viewAllPassengerInfo(AirlineService airlineService) {
        try {
            Map<String, String> allPassengerInfo = airlineService.getAllPassengerInfo();
            System.out.println("All Passenger Information:");

            if (allPassengerInfo.isEmpty()) {
                System.out.println("No passenger information available.");
            } else {
                for (Map.Entry<String, String> entry : allPassengerInfo.entrySet()) {
                    System.out.println(entry.getKey() + ": " + entry.getValue());
                }
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}