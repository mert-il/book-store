from models.author import Author 

class AuthorLogic(object):
    def save(self, author):
        try:
            if Author.objects(name=author.name).first() == None:
                author.save()
        except Exception as exception:
            raise exception

    def get(self, name):
        try:
            return Author.objects(name=name).first()
        except Exception as exception:
            raise exception