# Generated by Django 4.1 on 2022-08-24 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carsTestApp', '0026_alter_notification_client_not'),
    ]

    operations = [
        migrations.AddField(
            model_name='offre',
            name='expert',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='carsTestApp.expert'),
        ),
    ]
