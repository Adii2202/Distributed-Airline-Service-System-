from xmlrpc.client import ServerProxy

proxy = ServerProxy("http://localhost:3000")

if __name__ == "__main__":
    while True:
        print(
            """
            Choices available:
            1. View Flights
            2. Book a Flight
            3. Exit
            """
        )
        print("Enter your choice: ", end="")

        choice = int(input())
        if choice == 1:
            print(proxy.view_flights())
        elif choice == 2:
            id = input("Enter flight ID to book your flight:").strip()
            flight_class = input("Choose flight class (B-business, E-economy):").strip().upper()
            cost = proxy.bookFlight(id, flight_class)
            if input(f"Cost of flight-Rs. {cost}\nPay to book? [Y/N]: ").upper()[0] == "Y":
                proxy.pay(flight_class)
                print("Your flight has been booked")
            else:
                print("Booking successfully cancelled.")
        elif choice == 3:
            print("Happy Journey and visit again :)")
            break
        else:
            print("You have entered a wrong choice.")
# Can't Multithread client since it automatically runs parallel.
