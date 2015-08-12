# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('django_stormpath', '0002_auto_20150709_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=35, null=True)),
                ('region', models.CharField(max_length=35, null=True)),
                ('postal_code', models.CharField(max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=3)),
                ('calling_code', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('rate', models.FloatField()),
                ('from_currency', models.ForeignKey(related_name='exchange_rates', to='common.Currency')),
                ('to_currency', models.ForeignKey(to='common.Currency')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('authored_at', models.DateTimeField(null=True)),
                ('text', models.TextField(default=b'')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('stormpathuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('longitude', models.FloatField(null=True)),
                ('latitude', models.FloatField(null=True)),
                ('phone', models.CharField(max_length=16, null=True)),
                ('address', models.ForeignKey(to='common.Address', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('django_stormpath.stormpathuser', models.Model),
        ),
        migrations.AddField(
            model_name='note',
            name='author',
            field=models.ForeignKey(to='common.User'),
        ),
        migrations.AddField(
            model_name='country',
            name='currency',
            field=models.ForeignKey(related_name='countries', to='common.Currency'),
        ),
    ]
