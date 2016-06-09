# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-08 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20160606_0250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='capacity',
        ),
        migrations.AddField(
            model_name='offering',
            name='capacity',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]