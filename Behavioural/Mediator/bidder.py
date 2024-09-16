from colleague import Colleague
from auction import AuctionMediator


class Bidder(Colleague):
    def __init__(self, name: str, auction_mediator: AuctionMediator) -> None:
        self.name = name
        self.auction_mediator = auction_mediator
        self.auction_mediator.add_bidder(self)

    def get_name(self) -> str:
        return self.name

    def place_bid(self, amount: int) -> None:
        self.auction_mediator.place_bid(self, amount)

    def receive_bid_notification(self, amount: int) -> None:
        print(f"Bidder: {self.name} is to be informed that bid amount has changed to {amount}")
