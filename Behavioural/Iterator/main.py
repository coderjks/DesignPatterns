from typing import List

from Behavioural.Iterator.iterator import BooksIterator
from book import Book
from library import Library

if __name__ == '__main__':
    books: List[Book] = list()
    books.append(Book("Designing Data Intensive Applications", "MARTIN KAMPBELL"))
    books.append(Book("Think & Grow Rich", "NAPOLEON HILL"))

    library = Library("CITY CENTRAL LIBRARY", books)
    iterator: BooksIterator = library.create_iterator()

    while iterator.has_next():
        print(iterator.next())
