# Generated by Django 4.1.7 on 2023-02-16 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='inversion',
            field=models.FloatField(),
        ),
    ]
