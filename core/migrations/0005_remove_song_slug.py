# Generated by Django 4.0 on 2022-02-22 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_album_slug_song_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='slug',
        ),
    ]
