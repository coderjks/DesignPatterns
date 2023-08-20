from audi import Audi
from show import Show


class Theatre:
    def __init__(self, theatre_id: int, address: str):
        self.theatre_id = theatre_id
        self.address = address
        self.shows = list[Show]()
        self.audis = list[Audi]()

    def add_shows(self, show_list: list[Show]) -> None:
        self.shows.extend(show_list)

    def get_shows(self) -> list[Show]:
        return self.shows

    def remove_show(self, show_id) -> None:
        for show in self.shows:
            if show_id == show.show_id:
                self.shows.remove(show)
                break

    def add_audis(self, audi_list: list[Audi]) -> None:
        self.audis.extend(audi_list)

    def get_audis(self) -> list[Audi]:
        return self.audis

    def remove_audi(self, audi_id) -> None:
        for audi in self.audis:
            if audi_id == audi.audi_id:
                self.audis.remove(audi)
                break
