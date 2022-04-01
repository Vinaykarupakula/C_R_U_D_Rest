from pyexpat import model
from django.db import models

# Create your models here.
class BookModel(models.Model):
    name = models.CharField(max_length=30)
    numOfpages = models.BigIntegerField()
    author = models.CharField(max_length=50)
    typeOfbook = models.CharField(max_length=20)
    info = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

        

