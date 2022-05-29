from models.order import Order 

class OrderLogic(object):
    def save(self, order):
        try:
            order.save()
        except Exception as exception:
            raise Exception

    def get_by_user(self, user):
        try:
            return Order.objects(user=user)
        except Exception as exception:
            raise exception

        