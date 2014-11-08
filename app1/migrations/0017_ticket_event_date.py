# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_auto_20141106_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='event_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
