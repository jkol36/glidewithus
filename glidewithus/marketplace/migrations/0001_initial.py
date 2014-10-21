# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interest', models.CharField(max_length=250, null=True, blank=True)),
                ('company', models.CharField(max_length=250, null=True, blank=True)),
                ('profession', models.CharField(max_length=250, null=True, blank=True)),
                ('keyword', models.CharField(max_length=250, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
