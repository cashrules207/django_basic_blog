# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-16 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp', '-updated']},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
