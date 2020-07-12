from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
        The primary attributes of User are
        username
        password
        email
        first_name
        last_name
        """
    #will hold the the amount of money this customer has purchased before.
    value_of_items_purchased_before = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    def __str__(self):
        return f"{self.id}: username: {self.username} password: {self.password} email: {self.email} firstname: {self.first_name} last_name: {self.last_name}"



class Item(models.Model):

    item_description = models.CharField(max_length=200)
    item_name = models.CharField(max_length=64)
    item_price = models.DecimalField(max_digits=5, decimal_places=2, default=999.99)
    stock_available = models.IntegerField()

    def __str__(self):
        return f"{self.id}: name: {self.item_name} description: {self.item_description} price: {self.item_price} available: {self.stock_available}"



