# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20141030_0307'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='user_image',
            field=models.ImageField(null=True, upload_to=b'photos/user_photos', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'photos/event_thumbnails', blank=True),
            preserve_default=True,
        ),
    ]
