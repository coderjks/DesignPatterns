from theatre import Theatre
from collections import defaultdict


class TheatreController:
    def __init__(self):
        self.theatres_by_city = defaultdict(list)
        self.theatres = list()

    def add_theatre(self, theatre: Theatre, city: str) -> None:
        self.theatres.append(theatre)
        self.theatres_by_city[city.lower()].append(theatre)

    def get_theatres_by_city(self, city) -> list[Theatre]:
        return self.theatres_by_city[city.lower()]

    def get_theatre_by_name(self, theatre_name: str) -> Theatre:
        for theatre in self.theatres:
            if theatre.name.lower() == theatre_name.lower():
                return theatre
