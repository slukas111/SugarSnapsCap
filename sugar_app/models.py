from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from users.models import  Profile


# Create your models here.


class Categories(models.Model):
    category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category


class BoxItem(models.Model):
    Que_Choices = [
        ('Available', 'Available'),
        ('Pending', 'Pending'),
        ('Claimed', 'Claimed')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    expiration = models.DateTimeField()
    que_assign = models.CharField(default='Available', choices=Que_Choices, max_length=12)
    image = models.ImageField(default="default.jpg", upload_to="boxitem")
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    item_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    reserve = models.ManyToManyField(Profile, symmetrical=False, blank=True, related_name='reserving')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('postdetail', kwargs={'slug': self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = BoxItem.objects.filter(slug=slug).order_by('-id')
    exist = qs.exists()
    if exist:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_boxItem_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_boxItem_receiver, sender=BoxItem)
