# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-10 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='house_type',
            field=models.CharField(choices=[(1, 'Employee'), (1, 'Student')], default=1, max_length=10),
        ),
        migrations.AlterField(
            model_name='flat',
            name='preferred_guests',
            field=models.CharField(choices=[(1, 'Employee'), (1, 'Student')], max_length=10),
        ),
    ]
