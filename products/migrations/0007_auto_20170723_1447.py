# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-23 14:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170723_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='meds',
            field=models.ManyToManyField(related_name='ordered_meds', to='products.meds'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
