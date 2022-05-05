from models.genre import Genre
from services.exception import BasicException

class GenreLogic(object):
    def create(self, genre):
        try:
            if Genre.objects(name=genre.name).first() == None:
                genre.save()
                return genre 
        except Exception as e:
            raise BasicException(message = str(e), HTTPCode = 400) 

    def get_by_name(self, name):
        try:
            genre = Genre.objects(name=name).first()
            if genre == None:
                genre = self.create(Genre(name=name))
            return genre 
        except Exception as e:
            raise BasicException(message = str(e), HTTPCode = 400) 