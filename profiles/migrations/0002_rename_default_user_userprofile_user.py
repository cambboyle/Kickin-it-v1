# Generated by Django 4.2 on 2024-10-12 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='default_user',
            new_name='user',
        ),
    ]
