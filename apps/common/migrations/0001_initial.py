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
            name='User',
            fields=[
                ('stormpathuser_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('django_stormpath.stormpathuser',),
        ),
    ]
