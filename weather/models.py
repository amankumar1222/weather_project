from django.db import models

# Create your models here.

class City(models.Model):
    city = models.CharField(max_length=50)

    
    def __str__(self) :
        return self.city
