# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qie_cards', '0024_test_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='required',
            field=models.BooleanField(default=False),
        ),
    ]