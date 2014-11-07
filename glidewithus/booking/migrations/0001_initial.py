# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20141030_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='meetuprequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seen', models.BooleanField(default=False)),
                ('start_time', models.TimeField()),
                ('date', models.DateField()),
                ('message', models.TextField()),
                ('response', models.NullBooleanField()),
                ('target_recipient', models.ForeignKey(related_name=b'book_recipients', verbose_name=b'Booking Recipient', to='profiles.GlideProfile')),
                ('target_sender', models.ForeignKey(related_name=b'book_senders', verbose_name=b'Booking Initiator', to='profiles.GlideProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
