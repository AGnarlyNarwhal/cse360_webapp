# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20141028_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='Attendees', null=True, to='app1.Person', blank=True),
            preserve_default=True,
        ),
    ]
