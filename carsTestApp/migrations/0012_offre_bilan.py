# Generated by Django 4.1 on 2022-08-22 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carsTestApp', '0011_alter_offre_annee'),
    ]

    operations = [
        migrations.AddField(
            model_name='offre',
            name='bilan',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='carsTestApp.bilan_expert'),
        ),
    ]
