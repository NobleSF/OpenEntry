# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.common.utils
import django_extensions.db.fields.json
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('quantity', models.IntegerField(default=0)),
                ('colors', django_extensions.db.fields.json.JSONField(default=b'', blank=True)),
                ('width', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
                ('length', models.FloatField(null=True)),
                ('weight', models.FloatField(null=True)),
                ('price', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='ShippingOption',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'shipping options',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('slug', models.SlugField(null=True, blank=True)),
                ('published_at', models.DateTimeField(null=True, blank=True)),
                ('unpublished_at', models.DateTimeField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('subdomain', models.CharField(max_length=50, null=True, blank=True)),
                ('domain', models.CharField(max_length=100, null=True, blank=True)),
                ('default_currency', models.ForeignKey(to='common.Currency', null=True)),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name_plural': 'stores',
            },
        ),
        migrations.CreateModel(
            name='StoreCategory',
            fields=[
                ('slug', models.SlugField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('plural_name', models.CharField(max_length=50)),
                ('keywords', models.CharField(max_length=50, null=True, blank=True)),
                ('parent_category', models.ForeignKey(related_name='sub_categories', to='store.StoreCategory', null=True)),
                ('store', models.ForeignKey(related_name='categories', to='store.Store')),
            ],
            options={
                'verbose_name_plural': 'store categories',
            },
        ),
        migrations.CreateModel(
            name='StoreListing',
            fields=[
                ('valid_at', models.DateTimeField(null=True, blank=True)),
                ('expired_at', models.DateTimeField(null=True, blank=True)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('published_at', models.DateTimeField(null=True, blank=True)),
                ('unpublished_at', models.DateTimeField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('retail_price', apps.common.utils.DollarField(null=True, blank=True)),
                ('sale_price', apps.common.utils.DollarField(null=True, blank=True)),
                ('wholesale_price', apps.common.utils.DollarField(null=True, blank=True)),
                ('title', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.CharField(max_length=100, null=True, blank=True)),
                ('currency', models.ForeignKey(to='common.Currency', null=True)),
                ('product', models.OneToOneField(to='store.Product')),
                ('store', models.ForeignKey(related_name='listings', to='store.Store')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name_plural': 'store listings',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('product', models.ForeignKey(to='store.Product')),
            ],
            options={
                'verbose_name_plural': 'variants',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='products', to='store.StoreCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.ForeignKey(to='common.Currency', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_options',
            field=models.ManyToManyField(to='store.ShippingOption'),
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(related_name='products', to='store.Store'),
        ),
        migrations.AlterUniqueTogether(
            name='storecategory',
            unique_together=set([('store', 'name')]),
        ),
    ]
