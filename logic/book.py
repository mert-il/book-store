from models.book import Book
from services.exception import BasicException

class BookLogic(object):
    def create(book):
        try:
            if Book.objects(isban=book.isban).first() == None:
                book.save()
        except Exception as e:
            raise BasicException(message = str(e), HTTPCode = 400) 

    def get(id):
        try:
            return Book.objects(id=id).first()
        except Exception as e:
            raise BasicException(message = str(e), HTTPCode = 400)

    def get_all():
        try:
            return Book.objects()
        except Exception as e:
            raise BasicException(message = str(e), HTTPCode = 400) 

    def get_by_genre(genre):
        try:
            return Book.objects(genre=genre)
        except Exception as e:
            raise BasicException(message= str(e), HTTPCode= 400)