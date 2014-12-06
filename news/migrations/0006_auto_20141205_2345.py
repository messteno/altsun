# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20141205_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsimage',
            name='image',
            field=models.ImageField(upload_to=None),
            preserve_default=True,
        ),
    ]
