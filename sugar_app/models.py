from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Categories(models.Model):

    CATEGORY_CHOICES = [
        ('V', 'vegan'),
        ('G', 'vegetarian'),
        ('M', 'mixed'),
    ]

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)

    def __str__(self):
        return self.category


class BoxItem(models.Model):

    Que_Choices = [
        ('A', 'available'),
        ('P', 'pending'),
        ('C', 'claimed')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    expiration = models.DateTimeField()
    que_assign = models.CharField(default='available', choices=Que_Choices, max_length=1)
    image = models.ImageField(default="default.jpg", upload_to="boxitem")
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
