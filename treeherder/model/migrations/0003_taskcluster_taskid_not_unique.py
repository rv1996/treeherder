# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 15:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_add_taskcluster_job_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskclustermetadata',
            name='task_id',
            field=models.CharField(max_length=22, validators=[django.core.validators.MinLengthValidator(22)]),
        ),
    ]
