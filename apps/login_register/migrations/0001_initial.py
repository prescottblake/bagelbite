# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45)),
                ('pwhash', models.CharField(max_length=255)),
            ],
            managers=[
                ('userManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
