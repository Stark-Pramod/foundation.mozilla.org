# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-20 17:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_squashed_0013_remove_news_glyph'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='featured',
        ),
    ]