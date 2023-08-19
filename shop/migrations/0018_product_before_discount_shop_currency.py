# Generated by Django 4.1.5 on 2023-01-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_delete_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='before_discount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='shop',
            name='currency',
            field=models.CharField(choices=[('EGP', 'EGP'), ('USD', 'USD')], default=1, max_length=30),
            preserve_default=False,
        ),
    ]
