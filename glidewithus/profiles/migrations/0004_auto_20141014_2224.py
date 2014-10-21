# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_glideprofile_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bio',
            name='user',
        ),
        migrations.DeleteModel(
            name='Bio',
        ),
        migrations.AddField(
            model_name='glideprofile',
            name='traveler_pitch',
            field=models.CharField(default=None, max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='glideprofile',
            name='why_awesome',
            field=models.CharField(default=None, max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
    ]
