# Generated by Django 4.1.5 on 2023-01-31 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
