from models.genre import Genre 

class GenreLogic(object):
    def save(self, genre):
        try:
            if Genre.objects(name=genre.name).first() == None:
                genre.save()
        except Exception as exception:
            raise exception

    def get_all(self):
        try:
            return Genre.objects()
        except Exception as exception:
            raise exception

    def get(self, name):
        try:
            return Genre.objects(name=name).first()
        except Exception as exception:
            raise exception