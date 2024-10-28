from django.db import models
from django.db.models import DecimalField, TextField


# Create your models here.
# Модели с отношением "многие ко многим"
class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    size = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

    def __int__(self):
        return self.title