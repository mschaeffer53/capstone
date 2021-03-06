# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 00:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doggonnitapp', '0008_auto_20171214_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissingDogReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=25)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('description', models.TextField(default='')),
                ('weight', models.CharField(max_length=25)),
                ('age', models.CharField(max_length=25)),
                ('color', models.CharField(max_length=25)),
                ('breed', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='marker',
            name='dog',
        ),
        migrations.AlterField(
            model_name='dogprofile',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.DeleteModel(
            name='Marker',
        ),
        migrations.AddField(
            model_name='missingdogreport',
            name='dog',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='doggonnitapp.DogProfile'),
        ),
    ]
