# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.common.utils


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryEquivelence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'category equivelencies',
            },
        ),
        migrations.CreateModel(
            name='Marketplace',
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
                ('notes', models.ManyToManyField(to='common.Note')),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name_plural': 'marketplaces',
            },
        ),
        migrations.CreateModel(
            name='MarketplaceCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('plural_name', models.CharField(max_length=50)),
                ('keywords', models.CharField(max_length=50, null=True)),
                ('marketplace', models.ForeignKey(related_name='categories', to='marketplace.Marketplace')),
                ('parent_category', models.ForeignKey(related_name='sub_categories', to='marketplace.MarketplaceCategory', null=True)),
            ],
            options={
                'verbose_name_plural': 'marketplace categories',
            },
        ),
        migrations.CreateModel(
            name='MarketplaceListing',
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
                ('marketplace', models.ForeignKey(related_name='listings', to='marketplace.Marketplace')),
                ('product', models.OneToOneField(to='store.Product')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name_plural': 'marketplace listings',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valid_at', models.DateTimeField(null=True)),
                ('expired_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('marketplace', models.ForeignKey(to='marketplace.Marketplace')),
                ('notes', models.ManyToManyField(to='common.Note')),
                ('store', models.ForeignKey(to='store.Store')),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name_plural': 'memberships',
            },
        ),
        migrations.AddField(
            model_name='categoryequivelence',
            name='marketplace_category',
            field=models.ForeignKey(to='marketplace.MarketplaceCategory'),
        ),
        migrations.AddField(
            model_name='categoryequivelence',
            name='store_category',
            field=models.ForeignKey(to='store.StoreCategory'),
        ),
        migrations.AlterUniqueTogether(
            name='marketplacecategory',
            unique_together=set([('marketplace', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='categoryequivelence',
            unique_together=set([('marketplace_category', 'store_category')]),
        ),
    ]
