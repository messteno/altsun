# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsimage',
            options={'verbose_name_plural': 'изображения новостей', 'verbose_name': 'изображение новости'},
        ),
        migrations.RemoveField(
            model_name='news',
            name='images',
        ),
        migrations.AddField(
            model_name='newsimage',
            name='news',
            field=models.ForeignKey(to='news.News', null=True, blank=True),
            preserve_default=True,
        ),
    ]
