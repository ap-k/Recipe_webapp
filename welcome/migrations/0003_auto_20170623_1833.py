# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0002_main_course_1_main_course_2_main_course_3_main_course_4_main_course_5'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_course_1',
            name='recipe_name',
            field=models.CharField(default='abc', max_length=500),
        ),
        migrations.AddField(
            model_name='main_course_2',
            name='recipe_name',
            field=models.CharField(default='abc', max_length=500),
        ),
        migrations.AddField(
            model_name='main_course_3',
            name='recipe_name',
            field=models.CharField(default='abc', max_length=500),
        ),
        migrations.AddField(
            model_name='main_course_4',
            name='recipe_name',
            field=models.CharField(default='abc', max_length=500),
        ),
        migrations.AddField(
            model_name='main_course_5',
            name='recipe_name',
            field=models.CharField(default='abc', max_length=500),
        ),
    ]
