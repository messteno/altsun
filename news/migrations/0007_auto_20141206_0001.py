# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20141205_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsimage',
            name='image',
            field=models.ImageField(upload_to=news.models.get_news_image_path),
            preserve_default=True,
        ),
    ]
