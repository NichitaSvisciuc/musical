# Generated by Django 4.0 on 2022-02-22 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_song_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
