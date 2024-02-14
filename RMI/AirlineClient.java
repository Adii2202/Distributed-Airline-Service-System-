import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class AirlineClient {
    public static void main(String[] args) {
        try {
            // Get the registry
            Registry registry = LocateRegistry.getRegistry("localhost", 1098);

            // Look up the remote object from the registry
            AirlineService airlineService = (AirlineService) registry.lookup("AirlineService");

            // Create a Scanner for user input
            try (Scanner scanner = new Scanner(System.in)) {
                // Main menu for user interaction
                while (true) {
                    System.out.println("\n=== Airline Service ===");
                    System.out.println("1. Book Ticket");
                    System.out.println("2. Create Flight");
                    System.out.println("3. Delete Flight");
                    System.out.println("4. View Available Flights");
                    System.out.println("0. Exit");

                    System.out.print("Enter your choice: ");
                    int choice = scanner.nextInt();

                    switch (choice) {
                        case 1:
                            bookTicket(airlineService, scanner);
                            break;
                        case 2:
                            createFlight(airlineService, scanner);
                            break;
                        case 3:
                            deleteFlight(airlineService, scanner);
                            break;
                        case 4:
                            viewAvailableFlights(airlineService);
                            break;
                        case 0:
                            System.out.println("Exiting Airline Service client.");
                            System.exit(0);
                            break;
                        default:
                            System.out.println("Invalid choice. Please try again.");
                    }
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void bookTicket(AirlineService airlineService, Scanner scanner) {
        try {
            System.out.print("Enter passenger name: ");
            String passengerName = scanner.next();

            System.out.print("Enter flight number: ");
            int flightNumber = scanner.nextInt();

            String result = airlineService.bookTicket(passengerName, flightNumber);
            System.out.println(result);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void createFlight(AirlineService airlineService, Scanner scanner) {
        try {
            System.out.print("Enter flight number: ");
            int flightNumber = scanner.nextInt();

            System.out.print("Enter destination: ");
            String destination = scanner.next();

            System.out.print("Enter capacity: ");
            int capacity = scanner.nextInt();

            String result = airlineService.createFlight(flightNumber, destination, capacity);
            System.out.println(result);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void deleteFlight(AirlineService airlineService, Scanner scanner) {
        try {
            System.out.print("Enter flight number to delete: ");
            int flightNumber = scanner.nextInt();

            String result = airlineService.deleteFlight(flightNumber);
            System.out.println(result);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void viewAvailableFlights(AirlineService airlineService) {
        try {
            String result = airlineService.viewAvailableFlights();
            System.out.println(result);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
