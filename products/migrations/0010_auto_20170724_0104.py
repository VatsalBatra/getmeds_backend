# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-24 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20170724_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
