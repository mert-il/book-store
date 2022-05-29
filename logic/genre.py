from models.genre import Genre 

class GenreLogic(object):
    def save(self, genre):
        if Genre.objects(name=genre.name).first() == None:
            genre.save()

    def get_all(self) -> list:
        return Genre.objects()

    def get(self, name) -> Genre:
        return Genre.objects(name=name).first()