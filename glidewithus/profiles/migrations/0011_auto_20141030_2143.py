# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20141030_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glideprofile',
            name='profile_pic',
            field=sorl.thumbnail.fields.ImageField(default=None, null=True, upload_to=b'/images/profiles/profile_pics/', blank=True),
        ),
    ]
