from models.book import Book

class BookLogic(object):
    def save(self, book):
        try:
            if Book.objects(isban=book.isban).first() == None:
                book.save() 
        except Exception as exception:
            raise exception

    def get_all(self):
        try:
            return Book.objects() 
        except Exception as exception:
            raise exception

    def get_by_id(self, id):
        return Book.objects.get_or_404(id=id)

    def get_by_genre(self, genre):
        try:
            return Book.objects(genre=genre)
        except Exception as exception:
            raise exception