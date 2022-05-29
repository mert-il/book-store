from models.publisher import Publisher

class PublisherLogic(object):
    def save(self, publisher):
        if Publisher.objects(name=publisher.name).first() == None:
            publisher.save()

    def get(self, name) -> Publisher:
        return Publisher.objects(name=name).first()