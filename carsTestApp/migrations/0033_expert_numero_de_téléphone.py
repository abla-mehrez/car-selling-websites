# Generated by Django 4.1 on 2022-08-24 18:00

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('carsTestApp', '0032_alter_offre_bilan'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='numero_de_téléphone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
