# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='glideprofile',
            name='profile_pic',
        ),
    ]
