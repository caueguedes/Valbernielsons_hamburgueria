# Generated by Django 2.1.5 on 2019-01-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hamburgueria', '0005_produtopedido_qtd'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='image',
            field=models.CharField(default='', max_length=800),
        ),
    ]
