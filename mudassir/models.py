from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    def __str__(self):
       return self.name


# Create your models here.
