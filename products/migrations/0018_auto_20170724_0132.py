# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-24 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20170724_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='meds',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
