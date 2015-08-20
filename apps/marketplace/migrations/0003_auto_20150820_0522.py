# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.common.utils


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_auto_20150817_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketplace',
            name='domain',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='marketplace',
            name='published_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marketplace',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marketplace',
            name='subdomain',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='marketplace',
            name='unpublished_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marketplacecategory',
            name='keywords',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marketplacecategory',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marketplacelisting',
            name='description',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marketplacelisting',
            name='expired_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marketplacelisting',
            name='published_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marketplacelisting',
            name='retail_price',
            field=apps.common.utils.DollarField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marketplacelisting',
            name='sale_price',
            field=apps.common.utils.DollarField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marketplacelisting',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marketplacelisting',
            name='title',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marketplacelisting',
            name='unpublished_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marketplacelisting',
            name='valid_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='marketplacelisting',
            name='wholesale_price',
            field=apps.common.utils.DollarField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='membership',
            name='expired_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='membership',
            name='valid_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
