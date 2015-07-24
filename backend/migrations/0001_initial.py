# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateTimeField()),
                ('status', models.CharField(default=b'Received', max_length=2, choices=[(b'Received', b'Received'), (b'In Progress', b'In Progress'), (b'Completed', b'Completed'), (b'Shipped', b'Shipped')])),
                ('user', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='OrderSequence',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=50, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('librarySequence', models.TextField()),
                ('vectorSequence', models.TextField()),
                ('upstreamSequence', models.TextField()),
                ('downstreamSequence', models.TextField()),
                ('order', models.ForeignKey(related_name='+', to='backend.Order')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
