# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 04:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0009_rating_rate_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='rating',
            new_name='rating_int',
        ),
    ]
