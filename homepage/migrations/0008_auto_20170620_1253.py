# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20170329_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='examplemodel',
            name='name',
            field=models.CharField(default='default', max_length=120, primary_key=True, serialize=False),
        ),
    ]