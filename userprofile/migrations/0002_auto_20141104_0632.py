# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default=b'photos/profile_images/default_user.jpg', upload_to=b'photos/profile_images', blank=True),
            preserve_default=True,
        ),
    ]
