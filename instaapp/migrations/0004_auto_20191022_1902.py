# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-22 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0003_auto_20191022_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='instaapp.Profile'),
        ),
    ]
