# Generated by Django 4.1.7 on 2023-02-15 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_profile_email_profile_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Proffession',
            new_name='proffession',
        ),
    ]
