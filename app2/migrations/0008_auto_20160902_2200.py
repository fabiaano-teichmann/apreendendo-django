# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-03 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0007_auto_20160902_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]