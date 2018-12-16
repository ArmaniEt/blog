from django.db import models
from datetime import datetime


class User(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя пользователя')
    email = models.CharField(max_length=100, verbose_name='Почта')
    favorites = models.ManyToManyField('Article', blank=True, related_name='marked_by', verbose_name='Избранное')

    def __str__(self):
        return '%s %s' % (self.name, self.email)


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    author = models.ForeignKey(User, related_name='art_author', on_delete=models.PROTECT, verbose_name='Автор')
    text = models.TextField(max_length=3000, verbose_name='Текст статьи')
    created_at = models.DateField(default=datetime.now, verbose_name='Дата создания')

    def __str__(self):
        return self.title


class Comment(models.Model):
    commented_to = models.ForeignKey(Article, on_delete=models.CASCADE, null=True,
                                     related_name='comment_to', verbose_name='Комментарий к статье', blank=True)
    comment = models.TextField(max_length=1000, blank=True, verbose_name='Комментарий')
    commented_by = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE,
                                        verbose_name='Прокомментировано пользователем')
    comment_to_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='commented_comment',
                                           verbose_name='Комментарий к комментарию', blank=True, null=True)

    def __str__(self):
        return self.comment


class Rating(models.Model):
    RATING_PERFECTLY = 'perfectly'
    RATING_GOOD = 'good'
    RATING_NORMALLY = 'normally'
    RATING_BAD = 'bad'
    RATING_HORRIBLE = 'horrible'

    RATING_CHOICES = (
        (RATING_PERFECTLY, 'Отлично'),
        (RATING_GOOD, 'Хорошо'),
        (RATING_NORMALLY, 'Нормально'),
        (RATING_BAD, 'Плохо'),
        (RATING_HORRIBLE, 'Ужасно')
    )

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='art_rating', verbose_name='Статья')
    rating = models.CharField(max_length=30, choices=RATING_CHOICES, verbose_name='Оценка')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_rating', verbose_name='Пользователь')

    def __str__(self):
        return self.rating
