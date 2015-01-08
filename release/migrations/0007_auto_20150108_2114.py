# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0006_release_archive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='embed',
            field=models.TextField(blank=True, null=True, editable=False),
            preserve_default=True,
        ),
    ]
