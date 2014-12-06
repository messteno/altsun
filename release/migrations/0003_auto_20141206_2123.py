# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields
import release.models


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0002_auto_20141206_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=512)),
                ('biography', models.TextField(verbose_name='Биография')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArtistImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to=release.models.get_artists_image_path)),
                ('artist', models.ForeignKey(null=True, blank=True, to='release.Artist', related_name='images')),
            ],
            options={
                'verbose_name': 'изображение артиста',
                'verbose_name_plural': 'изображения артистов',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='release',
            options={'verbose_name': 'релизы и подкасты', 'verbose_name_plural': 'релизы и подкасты'},
        ),
        migrations.AlterField(
            model_name='release',
            name='podcast',
            field=models.BooleanField(verbose_name='Подкаст', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='release',
            name='release',
            field=embed_video.fields.EmbedVideoField(verbose_name='Ссылка'),
            preserve_default=True,
        ),
    ]
