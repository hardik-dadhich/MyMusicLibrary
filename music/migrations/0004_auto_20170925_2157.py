# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-25 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20170812_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='album_logo',
            field=models.FileField(default=' ', upload_to=b''),
        ),
    ]