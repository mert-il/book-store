from models.genre import Genre 

class GenreLogic(object):
    def save(self, genre: Genre):
        try:
            if Genre.objects(name=genre.name).first() == None:
                genre.save()
        except Exception as exception:
            raise exception

    def get_all(self) -> list[Genre]:
        try:
            return Genre.objects()
        except Exception as exception:
            raise exception

    def get(self, name: str) -> Genre:
        try:
            return Genre.objects(name=name).first()
        except Exception as exception:
            raise exception