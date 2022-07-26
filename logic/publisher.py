from models.publisher import Publisher

class PublisherLogic(object):
    def save(self, publisher: Publisher) -> None:
        try:
            if Publisher.objects(name=publisher.name).first() == None:
                publisher.save()
        except Exception as exception:
            raise exception

    def get(self, name: str) -> Publisher:
        try:
            return Publisher.objects(name=name).first()
        except Exception as exception:
            raise exception