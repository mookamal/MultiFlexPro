# Generated by Django 4.1.5 on 2023-01-31 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_alter_page_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='shop.webp', upload_to='product_images/%y/%m/%d'),
        ),
    ]
