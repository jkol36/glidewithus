# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('why_awesome', models.CharField(max_length=250, null=True, verbose_name=b'Why are you awesome', blank=True)),
                ('traveler_pitch', models.CharField(max_length=250, null=True, verbose_name=b'Why should a traveler want to meet up with you?', blank=True)),
                ('knowledge_on_city', models.CharField(max_length=2, choices=[(1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5'), (6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10')])),
                ('user', models.ManyToManyField(to='profiles.GlideProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
