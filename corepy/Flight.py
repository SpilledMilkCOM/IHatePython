"""Model for aircraft flights."""

class Flight:
    """A flight with a particular passenger aircraft."""

    def __init__(self, number, aircraft):
        
        # Establish the class invariants

        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}''")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}''")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid route number '{number}''")

        self._number = number
        self._aircraft = aircraft

        # Initialize all of the seats to None (vs occupied)
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        # Allows the client code to "reach through" the Flight to get the aircraft model
        # versus accessing the "private" _aircraft variable
        return self._aircraft.model()

    def airline(self):
        return self._number[:2]

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.

        Args:
            seat: A seat designator such as '12C' or '21F'
            passenger: The passnger name.

        Raises:
            ValueError: If the seat is unavailable.
        """
        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row][letter] = passenger

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._parse_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def num_available(self):
        return sum(sum(1 for seat in row.values() is seat is None)
                    for row in self._seating if row is not None)
    
    def number(self):
        return self._number

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat.

        Args:
            from_seat: The existing seat designator for the passenger to be moved.
            to_seat: The new seat designator.
        """
        from_row, from_letter = self._parse_seat(from_seat)

        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat {from_seat}")

       to_row, to_letter = self._parse_seat(to_seat)

        if self._seating[to_row][to_letter] is None:
            raise ValueError(f"Seat {to_seat} already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None


    #----==== PRIVATE ====-------------------------------------------------------------

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid row number {row}")

        return row, letter

    def _passenger_seats(self):
        """An iterable searies of passenger seating locations."""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None
                    yield (passenger, f"{row}{letter}")


#----==== MODULE FUNCTIONS ====----------------------------------------------------------

def console_card_printer(passenger, seat, flight_number, aircraft)
    output = f"| Name: {passenger}"         \
             f"  Flight: {flight_number}"   \
             f"  Seat: {seat}"              \
             f"  Aircraft: {aircraft}"      \
             " |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()