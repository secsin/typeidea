# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-06-13 17:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20220610_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
    ]
