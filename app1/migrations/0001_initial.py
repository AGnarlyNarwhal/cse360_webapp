# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateTimeField(verbose_name=b'event_date')),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('num_tickets', models.IntegerField()),
                ('description', models.CharField(max_length=5000)),
                ('picture', models.ImageField(upload_to=b'event_pics')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('events', models.ForeignKey(default=0, to='app1.Event')),
                ('person', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='Attendees', to='app1.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='host',
            field=models.ForeignKey(related_name='Event_Host', to='app1.Person'),
            preserve_default=True,
        ),
    ]
