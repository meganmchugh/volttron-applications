# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-16 18:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vtn', '0034_auto_20171116_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 16, 18, 37, 48, 921205), verbose_name='Report end'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 16, 18, 38, 4, 345681), verbose_name='Report start'),
            preserve_default=False,
        ),
    ]