# Generated by Django 4.1.5 on 2023-02-01 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_jobtitle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='gethub',
            new_name='github',
        ),
    ]
