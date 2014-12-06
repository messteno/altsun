# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='release',
            options={'verbose_name_plural': 'релизы', 'verbose_name': 'релиз'},
        ),
        migrations.AddField(
            model_name='release',
            name='podcast',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
