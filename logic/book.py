from models.book import Book 

class BookLogic(object):
    def save(self, book):
        if Book.objects(isban=book.isban).first() == None:
            book.save() 

    def get_all(self) -> list:
        return Book.objects() 

    def get_by_id(self, id) -> Book:
        return Book.objects.get_or_404(id=id)

    def get_by_genre(self, genre) -> list:
        return Book.objects(genre=genre)