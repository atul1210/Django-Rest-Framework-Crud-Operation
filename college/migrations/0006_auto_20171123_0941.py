# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0005_profile_aboutme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(upload_to='images'),
        ),
    ]
