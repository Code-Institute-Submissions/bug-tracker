# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-12 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugDB', '0005_delete_issueproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='issueProjectName',
            field=models.CharField(max_length=30),
        ),
    ]