# Generated by Django 4.1 on 2022-08-22 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsTestApp', '0013_alter_offre_bilan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='prix_enchere',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
