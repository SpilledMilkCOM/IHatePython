from abc import abstractmethod

class Aircraft:

    def __init__(self, registration):
        self._registration = registration

    def num_seats(self):
        # the linter is still complaining about this "abstract" class' self method
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

    def registration(self):
        return self._registration

    @abstractmethod
    def seating_plan(self):
        # if this is not defined, the linter will complain
        pass


class AircraftPreviousDefinition:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def model(self):
        return self._model

    def registration(self):
        return self._registration

    def seating_plan(self):
        return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])
