# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0005_release_embed'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='archive',
            field=models.FileField(blank=True, upload_to='/home/mesteno/Work/www/alt-sun.com/altsun/../media/releases/', null=True),
            preserve_default=True,
        ),
    ]
