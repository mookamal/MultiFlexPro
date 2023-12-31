# Generated by Django 4.1.5 on 2023-02-03 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_shop_is_brands_shop_is_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('is_father', models.BooleanField(default=False)),
                ('img', models.ImageField(default='categorise.webp', upload_to='categories')),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='shop.shop')),
                ('father', models.ForeignKey(blank=True, limit_choices_to={'is_father': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.categorie')),
            ],
        ),
    ]
