# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-11 18:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='album',
            new_name='album_pk',
        ),
    ]