# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(verbose_name='Название', max_length=512)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации', default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'новости',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.TextField()),
                ('image', models.ImageField(upload_to='img/news')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='news',
            name='images',
            field=models.ManyToManyField(to='news.NewsImage', blank=True, null=True),
            preserve_default=True,
        ),
    ]
