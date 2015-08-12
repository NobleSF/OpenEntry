# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='stormpathuser_ptr',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='address',
            new_name='line_1',
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='line_2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='line_3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
