from django.db import models
from django.urls import reverse



# Create your models here.





class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.TextField(max_length=250)
    production = models.IntegerField()
    image = models.ImageField(upload_to='main_app/static/uploads/', default='')


    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('details', kwargs={'car_id': self.id})
    


class Oil(models.Model):
    OILS = (
        ('M', 'Mumtaz'),
        ('J', 'Jayed'),
        ('S', 'Super')
    )
    date = models.DateField()
    type = models.CharField(max_length=1, choices=OILS)  
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_type_display()} on {self.date}"