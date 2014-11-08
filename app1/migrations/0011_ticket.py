# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0010_auto_20141104_0252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_tickets', models.IntegerField(default=b'0', null=True, blank=True)),
                ('customer', models.ForeignKey(related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(related_name='ticket_event', to='app1.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
