# Generated by Django 3.0 on 2019-12-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasien',
            name='keluhan',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='resep',
            name='nama_pasien',
            field=models.CharField(max_length=200),
        ),
    ]
