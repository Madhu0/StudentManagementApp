# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-31 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudentManagement', '0010_auto_20160731_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjectattendencetable',
            name='subject',
        ),
        migrations.AddField(
            model_name='subjectattendencetable',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='StudentManagement.Subject'),
        ),
    ]
