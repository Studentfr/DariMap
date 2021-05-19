from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class Drug(models.Model):
    name = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.name


class Pharmacy(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    address = models.CharField(max_length=150, default=True)
    phone_number = models.CharField(max_length=150, default=False)
    description = models.CharField(max_length=150, default=False)
    coordinate_id = models.ForeignKey('Coordinate', on_delete=models.PROTECT)
    user_id = models.ForeignKey('User', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, username, role_id, password=None):
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(username=username, role_id=role_id)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, password, username):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username,
            role_id=Role.get_role(self),
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, db_index=True, unique=True)
    password = models.CharField(max_length=150, default=False)
    role_id = models.ForeignKey('Role', on_delete=models.PROTECT)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


class Role(models.Model):
    rolename = models.CharField(max_length=150, default=True)

    def __str__(self):
        return self.rolename

    def get_role(self):
        try:
            admin = self.objects.get(rolename='Admin')
        except:
            admin = Role(rolename='Admin')
            admin.save()
        return admin


class Coordinate(models.Model):
    longitude = models.FloatField(max_length=150)
    latitude = models.FloatField(max_length=150)

    # def __float__(self):
    #     return self.latitude


class Pharmacy_Drug(models.Model):
    drug_id = models.ForeignKey('Drug', on_delete=models.PROTECT)
    pharmacy_id = models.ForeignKey('Pharmacy', on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.IntegerField()

    # def __int__(self):
    #     return self.amount


class Transaction(models.Model):
    pharmacy_id = models.ForeignKey('Pharmacy', on_delete=models.CASCADE)
    drug_id = models.ForeignKey('Drug', on_delete=models.CASCADE)
    pharmacy_drug_price = models.ForeignKey('Pharmacy_Drug', on_delete=models.CASCADE)
    amount = models.IntegerField()


class Favourite_Pharmacy(models.Model):
    pharmacy_id = models.ForeignKey('Pharmacy', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)


class Favourite_Drug(models.Model):
    drug_id = models.ForeignKey('Drug', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
