# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-26 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0038_auto_20170726_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_item',
            field=models.ManyToManyField(default='', related_name='item', to='products.cart_item'),
        ),
    ]
