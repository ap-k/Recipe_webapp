# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0006_auto_20170626_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='welcome_beverage_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient1', models.CharField(max_length=250)),
                ('recipe_name', models.CharField(max_length=500)),
                ('recipe_link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='beverage_1',
        ),
    ]