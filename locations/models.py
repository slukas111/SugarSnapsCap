from django.db import models

# Create your models here.


class Location(models.Model):
    address = models.TextField()

    def __str__(self):
        return self.address


class Area(models.Model):
    area_name = models.CharField(max_length=150)
    address = models.ManyToManyField(Location, blank=True)

    def __str__(self):
        return self.area_name
