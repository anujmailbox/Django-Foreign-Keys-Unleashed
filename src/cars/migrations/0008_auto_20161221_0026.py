# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 00:26
from __future__ import unicode_literals

import cars.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_auto_20161221_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(cars.models.set_delete_user), to=settings.AUTH_USER_MODEL),
        ),
    ]
