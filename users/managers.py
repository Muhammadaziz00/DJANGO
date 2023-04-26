from django.contrib.auth.base_user import BaseUserManager


class GeekUserManeger(BaseUserManager):
    def create_user(self, email, password, **exstra_fields):
        if not email:
            raise ValueError("Email должен быть обязателено!")
        email = self.normalize_email(email)
        user = self.model(email=email, **exstra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **exstra_fields):
        exstra_fields.setdefault("is_staff", True)
        exstra_fields.setdefault("is_superuser", True)
        exstra_fields.setdefault("is_active",True)
        if exstra_fields.get("is_staff") is not True:
            raise ValueError("суперпользователь должен иметьт статус is_staff = True")
        if exstra_fields.get("is_superuser") is not True:
            raise ValueError("суперпользователь должет иметь is_superuser = True")
        return self.create_user(email, password, **exstra_fields)