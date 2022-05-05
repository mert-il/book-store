from models.book import Book
from logic.author import AuthorLogic
from logic.publisher import PublisherLogic
from logic.genre import GenreLogic
from services.exception import BasicException

class BookLogic(object):
    def create(self, title, author, isban, publisher, genre, blurb, price, published_date):
        try:
            book = Book.objects(isban=isban).first()
            if book == None:
                author = AuthorLogic().get_by_name(author)
                publisher = PublisherLogic().get_by_name(publisher)
                genre = GenreLogic().get_by_name(genre)
                book = Book(
                    title = title,
                    author = author,
                    isban = isban,
                    publisher = publisher,
                    genre = genre,
                    blurb = blurb,
                    price = price,
                    published_date = published_date
                )
                book.save()
        except Exception as e:
            raise BasicException(message = str(e), HTTPCode = 400) 

    def get(self, id):
        try:
            return Book.objects(id=id).first()
        except Exception as e:
            raise BasicException(message = str(e), HTTPCode = 400)

    def get_all(self):
        try:
            return Book.objects()
        except Exception as e:
            raise BasicException(message = str(e), HTTPCode = 400) 

    def get_by_genre(self, genre_name):
        try:
            genre = GenreLogic().get_by_name(name=genre_name)
            return Book.objects(genre=genre)
        except Exception as e:
            raise BasicException(message= str(e), HTTPCode= 400)