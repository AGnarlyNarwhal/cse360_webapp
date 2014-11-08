# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0012_event_ticket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='num_tickets',
            new_name='t_num_tickets',
        ),
        migrations.RemoveField(
            model_name='event',
            name='ticket',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='event',
        ),
        migrations.AddField(
            model_name='ticket',
            name='t_customer',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='t_event',
            field=models.ForeignKey(blank=True, to='app1.Event', null=True),
            preserve_default=True,
        ),
    ]
