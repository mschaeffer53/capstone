# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doggonnitapp', '0007_auto_20171214_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]