# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=512, verbose_name='Название')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('create_date', models.DateTimeField(verbose_name='Дата публикации', default=django.utils.timezone.now, auto_now_add=True)),
                ('release', embed_video.fields.EmbedVideoField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
