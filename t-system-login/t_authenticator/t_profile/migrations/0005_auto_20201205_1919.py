# Generated by Django 3.1.4 on 2020-12-05 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t_profile', '0004_auto_20201205_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofle',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofle',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
    ]
