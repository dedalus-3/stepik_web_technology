# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.TextField(verbose_name='Тело ответа')),
                ('added_at', models.DateTimeField(verbose_name='Дата ответа', auto_now_add=True)),
                ('author', models.ForeignKey(verbose_name='Автор', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Заголовок', max_length=255)),
                ('text', models.TextField(verbose_name='Тело вопроса')),
                ('added_at', models.DateTimeField(verbose_name='Дата вопроса', auto_now_add=True)),
                ('rating', models.IntegerField(verbose_name='Рейтинг', default=0)),
                ('author', models.ForeignKey(verbose_name='Автор', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(verbose_name='Понравилось', blank=True, related_name='questions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(verbose_name='Вопрос', to='qa.Question'),
        ),
    ]
