from models.book import Book

def create_book(book):
    if Book.objects(isban=book.isban).first() == None:
        book.save()

def view_all_books():
    return Book.objects()

def view_by_genre(genre):
    return Book.objects(genre=genre)