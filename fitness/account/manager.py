from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, phone_no=None, weight=None, age=None, password=None):
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            username=username,
            phone_no=phone_no,
            weight=weight,
            age=age
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone_no=None, weight=None, age=None, password=None):
        user = self.create_user(
            username=username,
            phone_no=phone_no,
            weight=weight,
            age=age,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user