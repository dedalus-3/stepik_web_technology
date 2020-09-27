# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import iri_to_uri
from django.utils.http import urlquote
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
    """ Кастомизированный менеджер объектов """
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Тело вопроса')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата вопроса')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', blank=True, null=True)
    likes = models.ManyToManyField(User, blank=True, related_name='questions', verbose_name='Понравилось')

    # Custom Manager
    objects = QuestionManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        url = 'question/%s' % urlquote(self.id)
        return iri_to_uri(url)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    text = models.TextField(verbose_name='Тело ответа')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата ответа')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос', related_name='answer')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', blank=True, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'