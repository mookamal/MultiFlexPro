# Generated by Django 4.1.5 on 2023-01-19 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categorise',
            new_name='categorie',
        ),
    ]
