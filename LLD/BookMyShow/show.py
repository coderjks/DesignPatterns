from audi import Audi
from movie import Movie


class Show:
    def __init__(self, show_id: int, show_time: int, audi: Audi, movie: Movie) -> None:
        self.show_id = show_id
        self.show_time = show_time
        self.audi = audi
        self.movie = movie
        self.booked_seats = set[int]()
