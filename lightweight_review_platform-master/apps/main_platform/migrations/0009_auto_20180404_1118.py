# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-04 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_platform', '0008_auto_20180404_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='tags',
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='main_platform.Tag', verbose_name='标签'),
        ),
    ]
