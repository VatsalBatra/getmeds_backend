# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-24 11:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='meds',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]