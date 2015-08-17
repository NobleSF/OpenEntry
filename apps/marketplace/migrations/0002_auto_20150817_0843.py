# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.common.utils


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketplace',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='marketplacecategory',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='marketplacelisting',
            name='currency',
            field=models.ForeignKey(to='common.Currency', null=True),
        ),
        migrations.AlterField(
            model_name='marketplacelisting',
            name='retail_price',
            field=apps.common.utils.DollarField(null=True),
        ),
        migrations.AlterField(
            model_name='marketplacelisting',
            name='sale_price',
            field=apps.common.utils.DollarField(null=True),
        ),
        migrations.AlterField(
            model_name='marketplacelisting',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='marketplacelisting',
            name='wholesale_price',
            field=apps.common.utils.DollarField(null=True),
        ),
    ]
