# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_auto_20141106_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(default=b'photos/event_thumbnails/event_default.jpg', null=True, upload_to=b'photos/event_thumbnails', blank=True),
            preserve_default=True,
        ),
    ]
