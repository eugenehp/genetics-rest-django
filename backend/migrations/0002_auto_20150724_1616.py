# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'Received', max_length=20, choices=[(b'Received', b'Received'), (b'In Progress', b'In Progress'), (b'Completed', b'Completed'), (b'Shipped', b'Shipped')]),
        ),
        migrations.AlterField(
            model_name='ordersequence',
            name='order',
            field=models.ForeignKey(related_name='sequence', to='backend.Order'),
        ),
    ]
