from show import Show
from payment import Payment


class Booking:
    def __init__(self, booking_id: int, show: Show = None, booked_seats: list[int] = None, amount: int = None,
                 payment: Payment = None):
        self._booking_id = booking_id
        self._show = show
        self._booked_seats = booked_seats
        self._amount = amount
        self._payment = payment

    @property
    def show(self):
        return self._show

    @show.setter
    def show(self, value):
        self._show = value

    @property
    def booked_seats(self):
        return self._booked_seats

    @booked_seats.setter
    def booked_seats(self, value):
        self._booked_seats = value

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, value):
        self._payment = value
