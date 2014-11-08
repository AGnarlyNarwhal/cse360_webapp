# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ticket',
            field=models.ForeignKey(related_name='ticket', blank=True, to='app1.Ticket', null=True),
            preserve_default=True,
        ),
    ]
