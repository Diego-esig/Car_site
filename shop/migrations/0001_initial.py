# Generated by Django 4.0 on 2021-12-20 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=200)),
                ('modele', models.CharField(max_length=200)),
                ('categorie', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('prix', models.FloatField()),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]
