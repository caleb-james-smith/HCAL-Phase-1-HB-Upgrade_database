# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qie_cards', '0006_auto_20160603_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='attempt_num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]