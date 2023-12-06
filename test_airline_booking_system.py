import unittest
from unittest.mock import patch
from io import StringIO
import random
from airline_booking_system.airline2 import AirlineBookingSystem

class TestAirlineBookingSystem(unittest.TestCase):

    def test_booking_system(self):
        # Simulate user input
        user_input = [
            "1",  # Choose airline Dana Air
            "PHC",  # Choose destination PHC
            "one-way",  # Choose one-way trip
            "December 24th, 2023",  # Enter timeline
            "350000",  # Enter account balance
        ]

        with patch('builtins.input', side_effect=user_input), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Create an instance of the AirlineBookingSystem
            booking_system = AirlineBookingSystem()

            # Call the method to display destinations and proceed with booking
            booking_system.display_destinations()

            # Get the output
            output = mock_stdout.getvalue()

        # Assert statements for testing
        self.assertIn("You've selected ✈ Dana Air.", output)
        self.assertIn("You've selected Destination PHC.", output)
        self.assertIn("You've selected a one-way trip to Destination PHC.", output)
        self.assertIn("Checking the timeline for your one-way trip...\nThere is a flight available on December 24th, 2023.", output)
        self.assertIn("Checking for available tickets...\nGreat news! Tickets are available for your trip.", output)
        self.assertIn("Assigning you seat", output)
        self.assertIn("Congratulations! Your ticket has been booked.", output)

if __name__ == '__main__':
    unittest.main()
