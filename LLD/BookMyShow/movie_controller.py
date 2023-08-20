from movie import Movie
from collections import defaultdict


class MovieController:
    def __init__(self):
        self.movies_by_city = defaultdict(list)
        self.movies = list()

    def add_movie(self, movie: Movie, city: str) -> None:
        self.movies.append(movie)
        self.movies_by_city[city.lower()].append(movie)

    def get_movies_by_city(self, city) -> list[Movie]:
        return self.movies_by_city[city.lower()]

    def get_movie_by_name(self, movie_name: str) -> Movie:
        for movie in self.movies:
            if movie.name.lower() == movie_name.lower():
                return movie
