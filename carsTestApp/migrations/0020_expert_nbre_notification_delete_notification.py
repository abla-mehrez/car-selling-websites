# Generated by Django 4.1 on 2022-08-23 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsTestApp', '0019_remove_expert_nbre_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='nbre_notification',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
