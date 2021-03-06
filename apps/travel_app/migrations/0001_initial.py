# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 18:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=45)),
                ('start_date', models.CharField(max_length=45, null=True)),
                ('end_date', models.CharField(max_length=45, null=True)),
                ('description', models.CharField(max_length=140)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='login_register.User')),
            ],
        ),
        migrations.AddField(
            model_name='join',
            name='trip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travel_app.Trip'),
        ),
        migrations.AddField(
            model_name='join',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login_register.User'),
        ),
    ]
