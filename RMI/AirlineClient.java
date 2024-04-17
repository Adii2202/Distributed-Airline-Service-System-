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
            Scanner scanner = new Scanner(System.in);

            // Main menu for user interaction
            while (true) {
                System.out.println("\n=== Airline Service ===");
                System.out.println("1. Book Ticket");
                System.out.println("2. View Available Flights");
                System.out.println("3. Cancel Flight");
                System.out.println("4. View Passenger Booking Info");
                System.out.println("0. Exit");

                System.out.print("Enter your choice: ");
                int choice = scanner.nextInt();

                switch (choice) {
                    case 1:
                        bookTicket(airlineService, scanner);
                        break;
                    case 2:
                        viewAvailableFlights(airlineService);
                        break;
                    case 3:
                        cancelFlight(airlineService, scanner);
                        break;
                    case 4:
                        viewPassengerBookingInfo(airlineService, scanner);
                        break;
                    case 0:
                        System.out.println("Exiting Airline Service client.");
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

    private static void bookTicket(AirlineService airlineService, Scanner scanner) {
        try {
            System.out.print("Enter passenger name: ");
            String passengerName = scanner.next();

            System.out.print("Enter flight number: ");
            int flightNumber = scanner.nextInt();

            String result = airlineService.bookTicket(passengerName, flightNumber);

            // Display return ticket information and passenger details
            if (result.startsWith("Ticket booked")) {
                System.out.println(result);
                String returnTicketInfo = airlineService.getReturnTicketInfo(passengerName, flightNumber);
                String passengerInfo = airlineService.getPassengerInfo(passengerName, flightNumber);

                System.out.println("Return Ticket Information:\n" + returnTicketInfo);
                System.out.println("Passenger Information:\n" + passengerInfo);
            } else {
                System.out.println(result);
            }

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

    private static void cancelFlight(AirlineService airlineService, Scanner scanner) {
        try {
            System.out.print("Enter flight number to cancel: ");
            int flightNumber = scanner.nextInt();

            System.out.print("Enter your name: ");
            String passengerName = scanner.next();

            String result = airlineService.cancelTicket(passengerName, flightNumber);
            System.out.println(result);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void viewPassengerBookingInfo(AirlineService airlineService, Scanner scanner) {
        try {
            System.out.print("Enter passenger name: ");
            String passengerName = scanner.next();

            System.out.print("Enter flight number: ");
            int flightNumber = scanner.nextInt();

            String passengerInfo = airlineService.getPassengerInfo(passengerName, flightNumber);
            System.out.println("Passenger Booking Information:\n" + passengerInfo);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    
}