# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0007_auto_20150108_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='archive',
            field=models.FileField(blank=True, null=True, upload_to='releases'),
            preserve_default=True,
        ),
    ]
