from models.publisher import Publisher
from services.exception import BasicException

class PublisherLogic(object):
    def create(self, publisher):
        try:
            if Publisher.objects(name=publisher.name).first() == None:
                publisher.save()
                return publisher 
        except Exception as e:
            raise BasicException(message = str(e), HTTPCode = 400) 

    def get_by_name(self, name):
        try:
            publisher = Publisher.objects(name=name).first()
            if publisher == None:
                publisher = self.create(Publisher(name=name))
            return publisher 
        except Exception as e:
            raise BasicException(message = str(e), HTTPCode = 400) 