# Generated by Django 3.0.8 on 2020-07-28 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0002_auto_20200728_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nome_cat',
            field=models.CharField(max_length=50, verbose_name='Nome da Categoria'),
        ),
    ]
