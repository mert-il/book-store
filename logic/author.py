from models.author import Author
from services.exception import BasicException

class AuthorLogic(object):
    def create(self, author):
        try:
            if Author.objects(name=author.name).first() == None:
                author.save()
                return author 
        except Exception as e:
            raise BasicException(message = str(e), HTTPCode = 400) 

    def get_by_name(self, name):
        try:
            author = Author.objects(name=name).first()
            if author == None:
                author = self.create(Author(name=name))
            return author 
        except Exception as e:
            raise BasicException(message = str(e), HTTPCode = 400) 
