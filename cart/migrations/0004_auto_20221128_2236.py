# Generated by Django 2.2 on 2022-11-28 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_items_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='prodt',
            new_name='prod',
        ),
    ]