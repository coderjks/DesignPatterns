from abc import abstractmethod
from book import Book
from iterator import BooksIterator
from typing import List


class Aggregate:
    @abstractmethod
    def create_iterator(self):
        pass


class Library:
    def __init__(self, name, books: List[Book]):
        self.name = name
        self.books = books

    def create_iterator(self):
        return BooksIterator(self.books)
