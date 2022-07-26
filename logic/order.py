from models.order import Order 
from models.user import User

class OrderLogic(object):
    def save(self, order: Order) -> None:
        try:
            order.save()
        except Exception as exception:
            raise Exception

    def get_by_user(self, user: User) -> Order:
        try:
            return Order.objects(user=user)
        except Exception as exception:
            raise exception

        