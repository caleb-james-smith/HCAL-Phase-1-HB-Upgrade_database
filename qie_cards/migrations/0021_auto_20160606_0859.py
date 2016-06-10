# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 13:59
from __future__ import unicode_literals

from django.db import migrations, models
import qie_cards.models


class Migration(migrations.Migration):

    dependencies = [
        ('qie_cards', '0020_auto_20160603_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='image',
            field=models.ImageField(default='/default.png', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='qiecard',
            name='card_id',
            field=models.CharField(default='', max_length=7, validators=[qie_cards.models.validate_id]),
        ),
    ]