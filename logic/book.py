from models.book import Book 
from .base_logic import BaseLogic

class BookLogic(BaseLogic):

    def get_all(self):
        return Book.objects() 

    def get_by_id(self, id):
        return Book.objects.get_or_404(id=id)