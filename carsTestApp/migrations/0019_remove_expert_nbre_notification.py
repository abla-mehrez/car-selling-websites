# Generated by Django 4.1 on 2022-08-23 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carsTestApp', '0018_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expert',
            name='nbre_notification',
        ),
    ]
