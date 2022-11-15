from ctypes import addressof
from turtle import title
from django.db import models

# Create your models here.


class Listing(models.Model):  # listing model created; data below is table fields and their types
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    # image

    def __str__(self):  # returns the name of the model instead of referencing it as an object
        return self.title
