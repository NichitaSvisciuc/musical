# Generated by Django 4.0 on 2022-02-22 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_song_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='media'),
        ),
    ]
