# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-24 01:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20170724_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='title',
        ),
    ]
