# Generated by Django 2.1.5 on 2019-01-11 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hamburgueria', '0011_carrinho_qtd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrinho',
            old_name='owner_id',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='carrinho',
            old_name='produto_id',
            new_name='produto',
        ),
    ]
