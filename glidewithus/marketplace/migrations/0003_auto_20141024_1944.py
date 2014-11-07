# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_auto_20141024_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='company',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='search_company',
        ),
        migrations.AlterField(
            model_name='search',
            name='interest',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='search_interest',
        ),
        migrations.AlterField(
            model_name='search',
            name='keyword',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name='search_keyword',
        ),
        migrations.AlterField(
            model_name='search',
            name='profession',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='search_profession',
        ),
    ]
