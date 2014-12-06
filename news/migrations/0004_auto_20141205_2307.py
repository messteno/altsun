# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_remove_newsimage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(verbose_name='Содержание'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsimage',
            name='news',
            field=models.ForeignKey(null=True, blank=True, related_name='images', to='news.News'),
            preserve_default=True,
        ),
    ]
