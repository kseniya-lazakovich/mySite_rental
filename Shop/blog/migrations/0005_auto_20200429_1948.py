# Generated by Django 3.0.3 on 2020-04-29 16:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200429_1944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ('created',), 'verbose_name': 'Секция', 'verbose_name_plural': 'Секции'},
        ),
        migrations.AddField(
            model_name='section',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Создание'),
            preserve_default=False,
        ),
    ]