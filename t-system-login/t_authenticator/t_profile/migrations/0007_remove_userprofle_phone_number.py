# Generated by Django 3.1.4 on 2020-12-05 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('t_profile', '0006_userprofle_active_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofle',
            name='phone_number',
        ),
    ]
