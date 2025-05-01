from abc import ABC, abstractmethod
from typing import List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year}), {self.author}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: int):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def show_books(self):
        pass


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int):
        self.library.add_book(title, author, year)

    def remove_book(self, title: str):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()


class Library(LibraryInterface):
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, title: str, author: str, year: int):
        book = Book(title, author, year)
        self.books.append(book)
        logging.info(f'Book "{book.title}" added.')

    def remove_book(self, title: str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                logging.info(f'Book "{title}" removed!')
                return
        logging.warning(f'Book "{title}" not found!')

    def show_books(self):
        if not self.books:
            logging.info("The library is empty.")
            return
        logging.info("Library books:")
        for book in self.books:
            logging.info(book)


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        if command == "add":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            year_str = input("Enter book year: ").strip()
            try:
                year = int(year_str)
                manager.add_book(title, author, year)
            except ValueError:
                logging.warning("Invalid year format. Please enter a number.")
        elif command == "remove":
            title = input("Enter book title to remove: ").strip()
            manager.remove_book(title)
        elif command == "show":
            manager.show_books()
        elif command == "exit":
            logging.info("Exiting the library manager.")
            break
        else:
            logging.warning("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
