# Generated by Django 4.1.5 on 2023-01-14 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='لا يوجد وصف'),
        ),
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(default=' ', max_length=150),
        ),
    ]