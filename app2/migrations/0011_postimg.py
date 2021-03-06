# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-08 23:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0010_auto_20160903_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titulo da Imagen')),
                ('img', models.ImageField(upload_to=None)),
                ('id_img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.Post')),
            ],
        ),
    ]
