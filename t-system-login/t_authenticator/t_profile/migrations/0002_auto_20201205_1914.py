# Generated by Django 3.1.4 on 2020-12-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofle',
            name='email',
            field=models.EmailField(default=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='userprofle',
            name='location',
            field=models.TextField(default=True, null=True),
        ),
    ]
