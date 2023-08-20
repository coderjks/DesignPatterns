import datetime


class Movie:
    def __init__(self, name: str, release_date: datetime.date, duration: int) -> None:
        self.name = name
        self.release_date = release_date
        self.duration = duration
