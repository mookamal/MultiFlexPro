# Generated by Django 4.1.5 on 2023-01-22 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriesshop',
            name='slug',
        ),
    ]
