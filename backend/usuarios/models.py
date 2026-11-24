from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.


# UD5.1b - Manager del modelo MyUser
class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Ha de proporcionar un e-mail válido")

        user = self.model(
            email=self.normalize_email(email)
        )

        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    # UD5.1b - Creación de superusuarios
    def create_superuser(self, email, password):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Ha de proporcionar un e-mail válido")

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# UD5.1b - Modelo de usuario personalizado
class MyUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(unique=True)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = MyUserManager()