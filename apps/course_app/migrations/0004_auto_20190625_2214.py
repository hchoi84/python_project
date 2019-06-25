# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-25 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
        ('course_app', '0003_auto_20190625_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='likes',
        ),
        migrations.AddField(
            model_name='course',
            name='likes',
            field=models.ManyToManyField(related_name='courses_liked', to='user_app.User'),
        ),
    ]
