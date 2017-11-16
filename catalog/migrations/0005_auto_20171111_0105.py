# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20171109_1542'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={},
        ),
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
        migrations.RemoveField(
            model_name='bookinstance',
            name='due_back',
        ),
        migrations.AddField(
            model_name='book',
            name='due_back',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]