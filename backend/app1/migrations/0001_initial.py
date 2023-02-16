# Generated by Django 4.1.7 on 2023-02-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('tipologia', models.CharField(max_length=200)),
                ('titular', models.CharField(max_length=200)),
                ('inversion', models.IntegerField()),
                ('fecha', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=200)),
            ],
        ),
    ]