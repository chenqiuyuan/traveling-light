# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20170329_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examplemodel',
            name='id',
        ),
        migrations.AlterField(
            model_name='examplemodel',
            name='name',
            field=models.CharField(default='default', max_length=100, primary_key=True, serialize=False),
        ),
    ]