# Generated by Django 4.1.5 on 2023-06-08 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_alter_movie_model_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='movie_model',
            table='Movies',
        ),
    ]
