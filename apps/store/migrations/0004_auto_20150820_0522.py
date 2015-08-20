# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.common.utils
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20150820_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colors',
            field=django_extensions.db.fields.json.JSONField(default=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='domain',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='published_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='subdomain',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='unpublished_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='storecategory',
            name='keywords',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='storecategory',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='storelisting',
            name='description',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='storelisting',
            name='expired_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='storelisting',
            name='published_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='storelisting',
            name='retail_price',
            field=apps.common.utils.DollarField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='storelisting',
            name='sale_price',
            field=apps.common.utils.DollarField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='storelisting',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='storelisting',
            name='title',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='storelisting',
            name='unpublished_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='storelisting',
            name='valid_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='storelisting',
            name='wholesale_price',
            field=apps.common.utils.DollarField(null=True, blank=True),
        ),
    ]
