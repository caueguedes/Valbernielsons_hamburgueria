# Generated by Django 2.1.5 on 2019-01-10 16:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hamburgueria', '0004_auto_20190110_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtopedido',
            name='qtd',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
