# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-29 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20171129_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post/', verbose_name='Image'),
        ),
    ]
