# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-29 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20171128_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(upload_to='post/', verbose_name='Image'),
        ),
    ]
