from seat_type import SeatType


class Seat:
    def __init__(self, seat_id: int, seat_type: SeatType):
        self.seat_id = seat_id
        self.seat_type = seat_type
