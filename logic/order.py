from models.order import Order 

class OrderLogic(object):
    def save(self, order):
        order.save()