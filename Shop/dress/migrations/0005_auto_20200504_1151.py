# Generated by Django 3.0.3 on 2020-05-04 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dress', '0004_auto_20200504_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
    ]
