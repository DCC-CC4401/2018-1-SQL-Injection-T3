# Generated by Django 2.0.2 on 2018-07-07 22:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventario_cei', '0004_auto_20180705_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserve',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
