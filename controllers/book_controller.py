from models.book import Book
from services.exception import BasicException

def create_book(book):
    if Book.objects(isban=book.isban).first() == None:
        book.save()

def get_all_books():
    return Book.objects()

def get_by_genre(genre):
    return Book.objects(genre=genre)

def get_book(isban):
    try:
        return Book.objects(isban=isban).first()
    except Exception as e:
        raise BasicException(message = str(e), HTTPCode = 400)