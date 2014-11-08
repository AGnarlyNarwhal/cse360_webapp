# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_auto_20141104_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='t_customer',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='t_event',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='t_num_tickets',
            new_name='num_tickets',
        ),
    ]
