# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-25 02:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_remove_meds_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='meds',
        ),
    ]
