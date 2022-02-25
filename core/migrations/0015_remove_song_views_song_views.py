# Generated by Django 4.0 on 2022-02-25 07:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0014_song_song_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='views',
        ),
        migrations.AddField(
            model_name='song',
            name='views',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
