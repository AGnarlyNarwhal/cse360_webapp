# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auto_20141102_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='person',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
