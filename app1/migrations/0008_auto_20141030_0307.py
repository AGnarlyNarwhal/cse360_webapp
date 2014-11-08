# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20141028_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'/event_thumbnails', blank=True),
            preserve_default=True,
        ),
    ]
