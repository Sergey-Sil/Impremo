# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-27 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20171128_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='moder',
            field=models.BooleanField(default=False, verbose_name='Moder'),
        ),
        migrations.AddField(
            model_name='post',
            name='moder',
            field=models.BooleanField(default=False, verbose_name='Moder'),
        ),
    ]
