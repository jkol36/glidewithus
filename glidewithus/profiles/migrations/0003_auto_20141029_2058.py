# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20141029_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='glideprofile',
            name='questions',
        ),
        migrations.AddField(
            model_name='glideprofile',
            name='profile_pic',
            field=sorl.thumbnail.fields.ImageField(default=None, upload_to=b'images/profiles/profile_pics'),
            preserve_default=True,
        ),
    ]
