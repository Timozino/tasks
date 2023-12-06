import random

class AirlineBookingSystem:
    def __init__(self):
        # Welcome message
        print("Welcome to WAKA NOW")
        print("")

        # Define airline information
        self.airlines = {
            "Dana Air": {"LOS": 200_000, "PHC": 250_000, "ABJ": 300_000},
            "Peace Air": {"LOS": 180_000, "PHC": 220_000, "ABJ": 280_000},
            "Green Africa": {"LOS": 220_000, "PHC": 270_000, "ABJ": 320_000},
        }

        # Instance variables
        self.selected_airline = None
        self.destination_choice = None
        self.trip_type = None
        self.timeline = None

        # Display available airlines
        print("Available Airlines:")
        print("")

        for i, airline in enumerate(self.airlines.keys(), start=1):
            print(f"{i}. {airline}")

        print("")

        # Get user's choice of airline
        while True:
            try:
                choice = input("Please choose an airline (1, 2, or 3): ")
                if not choice.isdigit():
                    raise ValueError("Invalid input. Please enter a numeric choice.")

                user_choice = int(choice)

                if user_choice < 1 or user_choice > 3:
                    raise ValueError("Choice out of range")

                user_choice -= 1  # Adjusting for 0-based indexing
                self.selected_airline = list(self.airlines.keys())[user_choice]
                break
            except ValueError as e:
                print(f"{e} Please enter a valid numeric choice.")

    def display_destinations(self):
        # Display the selected airline
        print(f"You've selected ✈ {self.selected_airline}.\n")
        destinations = self.airlines[self.selected_airline]

        # Display available destinations for the selected airline
        print("Destinations:")
        for destination, cost in destinations.items():
            print(f"- {destination} (💸 N{cost})")

        # Get user's choice of destination
        while True:
            try:
                self.destination_choice = input("Please choose a destination (LOS, PHC, or ABJ): ").upper()
                if self.destination_choice not in ["LOS", "PHC", "ABJ"]:
                    raise ValueError("Invalid destination choice. Please try again.")

                print(f"You've selected Destination {self.destination_choice}.\n")
                self.trip_type = input("Do you want a one-way or two-way trip? ").lower()

                if self.trip_type not in ["one-way", "two-way"]:
                    raise ValueError("Invalid trip type. Please choose 'one-way' or 'two-way'.")
                
                print(f"You've selected a {self.trip_type} trip to Destination {self.destination_choice}.\n")
                self.timeline = input("Please enter the timeline for your trip: ")
                self.check_timeline()
                break
            except ValueError as e:
                print(f"{e}")

    def check_timeline(self):
        print(f"Checking the timeline for your {self.trip_type} trip...\nThere is a flight available on {self.timeline}.")

        tickets_available = True

        if tickets_available:
            # Tickets are available
            print("Checking for available tickets...\nGreat news! Tickets are available for your trip.")
            self.assign_seat()
        else:
            # No tickets available
            print("Sorry, no ticket is available for your trip.")

    def assign_seat(self):
        seat = self.generate_random_seat()
        print(f"Assigning you seat {seat} for your {self.trip_type} trip to Destination {self.destination_choice}.\n")

        # Get user's account balance
        account_balance = float(input("Now, please provide your account balance: 💸💸 N"))
        self.book_ticket(account_balance)

    def generate_random_seat(self):
        # Generate a random seat number, e.g., '12A'
        rows = list(range(1, 31))  # Assuming 30 rows
        row = random.choice(rows)
        seat_letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        return f"{row}{seat_letter}"

    def book_ticket(self, account_balance):
        if self.selected_airline in self.airlines:
            # Check if the selected airline exists
            print(f"Airline {self.selected_airline} exists.\n")

            trip_cost = self.airlines[self.selected_airline][self.destination_choice]

            if account_balance >= trip_cost:
                # Sufficient funds to book the ticket
                print(f"Checking your account balance...\nYour account balance is N{account_balance}.")
                print(f"The {self.trip_type} ticket to Destination {self.destination_choice} costs N{trip_cost}.")

                print("You have enough funds to book the ticket.")
                print("Congratulations! Your ticket has been booked.")
            else:
                # Insufficient funds
                print("You don't have sufficient funds to book the ticket. Please top up your account.")
        else:
            # Selected airline does not exist
            print("The selected airline does not exist.")


# Create an instance of the AirlineBookingSystem
booking_system = AirlineBookingSystem()

# Call the method to display destinations and proceed with booking
booking_system.display_destinations()
