from models.book import Book
from models.genre import Genre

class BookLogic(object):
    def save(self, book: Book) -> None:
        try:
            if Book.objects(isban=book.isban).first() == None:
                book.save() 
        except Exception as exception:
            raise exception

    def get_all(self) -> list[Book]:
        try:
            return Book.objects() 
        except Exception as exception:
            raise exception

    def get_by_id(self, id: str) -> Book:
        return Book.objects.get_or_404(id=id)

    def get_by_genre(self, genre: Genre) -> Book:
        try:
            return Book.objects(genre=genre)
        except Exception as exception:
            raise exception