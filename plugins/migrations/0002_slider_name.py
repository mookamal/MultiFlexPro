# Generated by Django 4.1.5 on 2023-01-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
