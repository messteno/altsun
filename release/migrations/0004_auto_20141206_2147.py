# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0003_auto_20141206_2123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name_plural': 'артисты', 'verbose_name': 'артист'},
        ),
        migrations.AddField(
            model_name='release',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, to='release.Artist', related_name='releases'),
            preserve_default=True,
        ),
    ]
