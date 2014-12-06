# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20141205_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsimage',
            name='image',
            field=models.ImageField(upload_to='34dfe564-3794-487b-9f2e-3580dbc38ef0.news'),
            preserve_default=True,
        ),
    ]
