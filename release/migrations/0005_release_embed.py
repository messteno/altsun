# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0004_auto_20141206_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='embed',
            field=models.TextField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
