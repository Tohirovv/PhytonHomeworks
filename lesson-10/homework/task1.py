class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException("Member cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException("This book is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if not book:
            raise BookNotFoundException("Book not found in the library.")
        if not member:
            raise Exception("Member not found.")
        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)
        if member and book:
            member.return_book(book)