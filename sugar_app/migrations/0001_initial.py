# Generated by Django 3.0.6 on 2020-07-16 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='Mixed', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BoxItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiration', models.DateTimeField()),
                ('que_assign', models.CharField(choices=[('Available', 'Available'), ('Pending', 'Pending'), ('Claimed', 'Claimed')], default='Available', max_length=12)),
                ('image', models.ImageField(default='default.jpg', upload_to='boxitem')),
                ('slug', models.SlugField(unique=True)),
                ('item_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sugar_app.Categories')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reserve', models.ManyToManyField(blank=True, related_name='reserving', to='users.Profile')),
            ],
        ),
    ]
