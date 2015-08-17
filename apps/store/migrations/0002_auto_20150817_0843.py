# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.common.utils


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='storecategory',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='storelisting',
            name='currency',
            field=models.ForeignKey(to='common.Currency', null=True),
        ),
        migrations.AlterField(
            model_name='storelisting',
            name='retail_price',
            field=apps.common.utils.DollarField(null=True),
        ),
        migrations.AlterField(
            model_name='storelisting',
            name='sale_price',
            field=apps.common.utils.DollarField(null=True),
        ),
        migrations.AlterField(
            model_name='storelisting',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='storelisting',
            name='wholesale_price',
            field=apps.common.utils.DollarField(null=True),
        ),
    ]
