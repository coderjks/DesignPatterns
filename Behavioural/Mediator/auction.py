from colleague import Colleague
from typing import List


class AuctionMediator:

    def add_bidder(self, bidder: Colleague):
        pass

    def place_bid(self, bidder: Colleague, bid_amount: int):
        pass


class Auction(AuctionMediator):
    def __init__(self):
        self.colleagues: List[Colleague] = list()

    def add_bidder(self, bidder):
        self.colleagues.append(bidder)

    def place_bid(self, bidder, bid_amount):
        for colleague in self.colleagues:
            if colleague.get_name() != bidder.get_name():
                colleague.receive_bid_notification(bid_amount)
