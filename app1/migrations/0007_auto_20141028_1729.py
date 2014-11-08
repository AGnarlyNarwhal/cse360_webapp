# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20141028_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='Attendees', null=True, to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='host',
            field=models.ForeignKey(related_name='Event_Host', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'photos/event_thumbnails', blank=True),
            preserve_default=True,
        ),
    ]
