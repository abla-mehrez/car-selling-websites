# Generated by Django 4.1 on 2022-08-20 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsTestApp', '0006_alter_commentaire_acheteur_alter_offre_vendeur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='image',
            field=models.ImageField(blank=True, upload_to='cars/fichier/images'),
        ),
    ]
