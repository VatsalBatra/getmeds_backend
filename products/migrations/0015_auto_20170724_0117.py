# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-24 01:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0014_auto_20170724_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='meds',
            field=models.ManyToManyField(default='', related_name='ordered_meds', to='products.meds'),
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='rate',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
