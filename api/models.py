from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()

 # to return  name of a new user
  def __str__(self):
    return self.name