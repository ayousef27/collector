from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.TextField(max_length=250)
    production = models.IntegerField()
    image = models.ImageField(upload_to='main_app/static/uploads/', default='')