# Generated by Django 3.2.7 on 2021-09-25 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_produto_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='ref',
            new_name='descricao',
        ),
    ]