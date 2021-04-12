from django.db import models


class Drug(models.Model):
    name = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.name


class Pharmacy(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    address = models.CharField(max_length=150, default=True)
    coordinate_id = models.ForeignKey('Coordinate', on_delete=models.PROTECT)
    user_id = models.ForeignKey('User', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=150, db_index=True)
    password = models.CharField(max_length=150, default=False)
    role_id = models.ForeignKey('Role', on_delete=models.PROTECT)

    def __str__(self):
        return self.username


class Role(models.Model):
    rolename = models.CharField(max_length=150, default=True)

    def __str__(self):
        return self.rolename


class Coordinate(models.Model):
    longitude = models.FloatField(max_length=150)
    latitude = models.FloatField(max_length=150)

    # def __float__(self):
    #     return self.latitude


class Pharmacy_Drug(models.Model):
    drug_id = models.ForeignKey('Drug', on_delete=models.PROTECT)
    pharmacy_id = models.ForeignKey('Pharmacy', on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.IntegerField(unique=True)

    # def __int__(self):
    #     return self.amount


class Transaction(models.Model):
    pharmacy_id = models.ForeignKey('Pharmacy', on_delete=models.CASCADE)
    drug_id = models.ForeignKey('Drug', on_delete=models.CASCADE)
    pharmacy_drug_price = models.ForeignKey('Pharmacy_Drug', on_delete=models.CASCADE, to_field='price')
    amount = models.IntegerField()


class Favourite_Pharmacy(models.Model):
    pharmacy_id = models.ForeignKey('Pharmacy', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)


class Favourite_Drug(models.Model):
    drug_id = models.ForeignKey('Drug', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
