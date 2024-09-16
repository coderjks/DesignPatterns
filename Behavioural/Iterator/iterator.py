from book import Book
from typing import List
from abc import abstractmethod


class Iterator:
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


class BooksIterator(Iterator):
    def __init__(self, books: List[Book]):
        self.books = books
        self.index = 0

    def has_next(self):
        return self.index < len(self.books)

    def next(self):
        if self.has_next():
            self.index += 1
            # to return the current index ele before incrementing
            return self.books[self.index - 1]
