from enum import Enum


class PaymentStatus(Enum):
    SUCCESS = 1
    FAILURE = 2
    PENDING = 3
    IN_PROGRESS = 4


class Payment:

    def __init__(self, payment_id: int, status: PaymentStatus):
        self.payment_id = payment_id
        self.status = status
