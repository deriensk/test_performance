# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-07 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0009_auto_20161206_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='full_mark',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='subject',
            name='mark_obtained',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='pass_mark',
            field=models.IntegerField(default=45),
        ),
        migrations.AddField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]