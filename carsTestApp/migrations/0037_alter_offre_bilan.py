# Generated by Django 4.1 on 2022-08-28 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carsTestApp', '0036_alter_offre_bilan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='bilan',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voiture_associée', to='carsTestApp.bilan_expert'),
        ),
    ]
