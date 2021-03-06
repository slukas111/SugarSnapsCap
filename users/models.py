from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import sys
sys.path.append('..')
from locations.models import Area


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    one_click_reserve = models.BooleanField(default=False)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='following')
    bio = models.TextField( null=True)
    location = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
