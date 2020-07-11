# Generated by Django 3.0.6 on 2020-07-10 03:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('one_click_reserve', models.BooleanField(default=False)),
                ('bio', models.CharField(max_length=500, null=True)),
                ('followers', models.ManyToManyField(blank=True, related_name='following', to='users.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
