from abc import ABC, abstractmethod

class BaseLogic(ABC):
    @abstractmethod
    def save(self, model):
        pass 

    @abstractmethod
    def get_by_id(self, id):
        pass 

    @abstractmethod
    def update(self, id, model):
        pass 

    @abstractmethod
    def delete(self, id):
        pass