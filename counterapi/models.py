from django.db import models

# Create your models here.

class Counter(models.Model):
    name = models.IntegerField(max_length=60)
    latitube = models.CharField(max_length=60)
    longitude = models.CharField(max_length=60)
    geography = models.CharField(max_length=1000)


    def __str__(self):
        return self.name
