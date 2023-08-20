from movie import Movie
from theatre import Theatre
from show import Show
from movie_controller import MovieController
from theatre_controller import TheatreController
from audi import Audi
from seat import Seat, SeatType
from booking import Booking
from payment import Payment, PaymentStatus
from collections import defaultdict
from datetime import datetime


class BookMyShow:
    def __init__(self):
        self.movie_controller = MovieController()
        self.theatre_controller = TheatreController()
        self.initialize()

    def initialize(self):
        self.create_movies()
        self.create_theatres()

    def book_show(self, city: str, movie_name: str):
        # 1. Get movies in the city and check if interested movie is there
        movies = self.movie_controller.get_movies_by_city(city)
        interested_movie = None
        for movie in movies:
            if movie.name.lower() == movie_name.lower():
                interested_movie = movie
                break

        if not interested_movie:
            print('This movie is not being shown in your city!!')
            return

        # 2. Get list of all the theatres and check if any show is there for this movie
        theatres = self.theatre_controller.get_theatres_by_city(city)
        available_shows = defaultdict(list)

        for theatre in theatres:
            theatre_shows = theatre.get_shows()
            for show in theatre_shows:
                if show.movie == interested_movie:
                    available_shows[theatre].append(show)

        # 3. select the show
        selected_show = available_shows.popitem()[1][0]

        # 4. reserve seat
        selected_seats = [30, 40]
        booked_seats = selected_show.booked_seats
        if any(seat_id in selected_seats for seat_id in booked_seats):
            print('Seats already selected')
            return

        # 5. Initiate payment
        booking_amount = 10 * len(selected_seats)

        booking = Booking(1, selected_show)
        payment = Payment(1, PaymentStatus.SUCCESS)
        booking.amount = booking_amount
        booking.payment = payment
        booking.booked_seats = selected_seats
        # selected_show.booked_seats.add()

        print('Seats booked successfully!!')

    def create_movies(self):
        movie_1 = Movie('Avenger', datetime(2017, 10, 1).date(), 150)
        movie_2 = Movie('Batman', datetime(2012, 6, 1).date(), 180)
        movie_3 = Movie('SpiderMan', datetime(2012, 6, 1).date(), 120)

        self.movie_controller.add_movie(movie_1, 'Delhi')
        self.movie_controller.add_movie(movie_2, 'Delhi')
        self.movie_controller.add_movie(movie_3, 'Noida')

    def create_theatres(self):
        pvr_theatre = Theatre(1, 'Logix Mall Noida, Noida')
        inox_theatre = Theatre(2, 'Select City Walk, Saket, Delhi')
        self.theatre_controller.add_theatre(pvr_theatre, 'Noida')
        self.theatre_controller.add_theatre(inox_theatre, 'Delhi')

        # add audis
        audi_1 = Audi(1, 50, BookMyShow.create_seats(50))
        audi_2 = Audi(2, 100, BookMyShow.create_seats(100))
        audi_3 = Audi(3, 70, BookMyShow.create_seats(70))
        audi_4 = Audi(4, 80, BookMyShow.create_seats(80))

        pvr_theatre.add_audis([audi_1, audi_2])
        inox_theatre.add_audis([audi_3, audi_4])

        # create shows
        avenger_movie = self.movie_controller.get_movie_by_name('Avenger')
        batman_movie = self.movie_controller.get_movie_by_name('Batman')
        spiderman_movie = self.movie_controller.get_movie_by_name('SpiderMan')

        show_1 = Show(1, 8, audi_1, avenger_movie)
        show_2 = Show(2, 8, audi_2, batman_movie)
        show_3 = Show(3, 11, audi_2, spiderman_movie)
        show_4 = Show(4, 10, audi_3, avenger_movie)
        show_5 = Show(5, 10, audi_4, batman_movie)
        show_6 = Show(6, 12, audi_4, spiderman_movie)

        # add shows
        pvr_theatre.add_shows([show_1, show_2, show_3])
        inox_theatre.add_shows([show_4, show_5, show_6])

    @staticmethod
    def create_seats(capacity: int) -> list[Seat]:
        seats = list()
        for i in range(1, capacity + 1):
            if 0 < i <= 10:
                seat_type = SeatType.RECLINER
            elif 10 < i <= 20:
                seat_type = SeatType.GOLD
            elif 20 < i <= 30:
                seat_type = SeatType.SILVER
            else:
                seat_type = SeatType.STANDARD

            seat = Seat(i, seat_type)
            seats.append(seat)

        return seats


if __name__ == "__main__":
    book_my_show = BookMyShow()
    book_my_show.book_show('delhi', 'avenger')
