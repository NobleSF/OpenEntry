# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=35, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='line_1',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='line_2',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='line_3',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(max_length=35, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='calling_code',
            field=models.CharField(max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(max_length=3, blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='authored_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(default=b'', blank=True),
        ),
    ]
