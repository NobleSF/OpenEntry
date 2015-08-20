# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20150817_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='domain',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='subdomain',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
