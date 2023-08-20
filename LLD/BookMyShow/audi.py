from seat import Seat


class Audi:
    def __init__(self, audi_id: int, capacity: int, seats: list[Seat] = []):
        self.audi_id = audi_id
        self.capacity = capacity
        self.seats = seats
