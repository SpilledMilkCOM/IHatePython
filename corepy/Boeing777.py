from Aircraft import Aircraft


class Boeing777(Aircraft):

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        # For simplicity's sake, we ignore complex seating arrangement for first-class
        return range(1, 56), "ABCDEGHJK"