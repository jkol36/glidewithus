# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_auto_20141030_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('seen', models.NullBooleanField(default=False)),
                ('recipient', models.ForeignKey(related_name=b'recieved_messages', verbose_name=b'Reciever', to='profiles.GlideProfile')),
                ('sender', models.ForeignKey(related_name=b'sent_messages', verbose_name=b'Sender', to='profiles.GlideProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
