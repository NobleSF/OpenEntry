# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.common.utils
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=0)),
                ('colors', django_extensions.db.fields.json.JSONField()),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'shipping options',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('published_at', models.DateTimeField(null=True)),
                ('unpublished_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('subdomain', models.CharField(max_length=50)),
                ('domain', models.CharField(max_length=100)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('plural_name', models.CharField(max_length=50)),
                ('keywords', models.CharField(max_length=50, null=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valid_at', models.DateTimeField(null=True)),
                ('expired_at', models.DateTimeField(null=True)),
                ('slug', models.SlugField()),
                ('published_at', models.DateTimeField(null=True)),
                ('unpublished_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('retail_price', apps.common.utils.DollarField()),
                ('sale_price', apps.common.utils.DollarField()),
                ('wholesale_price', apps.common.utils.DollarField()),
                ('title', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('currency', models.ForeignKey(to='common.Currency')),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
            field=models.ForeignKey(to='store.Store'),
        ),
        migrations.AlterUniqueTogether(
            name='storecategory',
            unique_together=set([('store', 'name')]),
        ),
    ]
