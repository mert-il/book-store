from models.admin import Admin
from services.encryption import generate_hash

class AdminLogic(object):
    def save(self, admin: Admin) -> None:
        try:
            if Admin.objects(email=admin.email).first() == None:
                admin.password = generate_hash(admin.password)
                admin.save()
        except Exception as exception:
            raise exception

    def get(self, email: str, password: str) -> Admin:
        try:
            password_hash = generate_hash(password)
            admin = Admin.objects(email=email, password=password_hash).first()
            return admin
        except Exception as exception:
            raise exception

    def get_by_id(self, id: str) -> Admin:
        return Admin.objects.get_or_404(id=id)