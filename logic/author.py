from models.author import Author 

class AuthorLogic(object):
    def save(self, author):
        if Author.objects(name=author.name).first() == None:
            author.save()

    def get(self, name) -> Author:
        return Author.objects(name=name).first()