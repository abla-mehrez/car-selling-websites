# Generated by Django 4.1 on 2022-08-24 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsTestApp', '0021_remove_expert_nbre_notification_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='nbre',
        ),
        migrations.AddField(
            model_name='notification',
            name='number',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
