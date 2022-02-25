# Generated by Django 4.0 on 2022-02-22 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.AddField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(to='core.Song'),
        ),
    ]
