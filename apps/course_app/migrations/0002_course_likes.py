# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-25 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]