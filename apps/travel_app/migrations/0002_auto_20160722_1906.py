# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0001_initial'),
        ('travel_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='join',
            name='user',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='user',
            new_name='author',
        ),
        migrations.AddField(
            model_name='trip',
            name='joiners',
            field=models.ManyToManyField(null=True, related_name='joiners', to='login_register.User'),
        ),
        migrations.DeleteModel(
            name='Join',
        ),
    ]
