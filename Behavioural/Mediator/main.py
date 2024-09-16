from auction import Auction, AuctionMediator
from colleague import Colleague
from bidder import Bidder

if __name__ == "__main__":

    auction_mediator: AuctionMediator = Auction()
    bidder1: Colleague = Bidder("Jitendra", auction_mediator)
    bidder2: Colleague = Bidder("Priyanka", auction_mediator)
    bidder3: Colleague = Bidder("Vishal", auction_mediator)

    bidder1.place_bid(100)
    bidder2.place_bid(200)
    bidder3.place_bid(300)



