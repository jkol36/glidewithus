# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20141014_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glideprofile',
            name='age',
            field=models.DateField(default=None, null=True, verbose_name=b'age', blank=True),
        ),
        migrations.AlterField(
            model_name='glideprofile',
            name='city',
            field=models.CharField(default=False, max_length=250, null=True, verbose_name=b'City', blank=True),
        ),
        migrations.AlterField(
            model_name='glideprofile',
            name='mission_statement',
            field=models.CharField(default=None, max_length=250, null=True, blank=True),
        ),
    ]
