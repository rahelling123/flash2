# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20170128_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='comment',
            field=models.TextField(default='this is great', max_length=500),
        ),
    ]
