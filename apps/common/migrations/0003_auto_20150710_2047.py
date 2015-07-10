# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=35, null=True, blank=True)),
                ('region', models.CharField(max_length=35, null=True, blank=True)),
                ('postal_code', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 10, 20, 46, 58, 920208, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 10, 20, 47, 5, 688163, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.ForeignKey(to='common.Address', null=True),
        ),
    ]
