# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20141029_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glideprofile',
            name='profile_pic',
            field=models.ImageField(default=None, null=True, upload_to=b'images/profiles/profile_pics', blank=True),
        ),
    ]
