from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя пользователя')
    email = models.CharField(max_length=100, verbose_name='Почта')
    favorites = models.ManyToManyField('Article', blank=True, related_name='marked_by', verbose_name='Избранное')

    def __str__(self):
        return '%s %s' % (self.name, self.email)


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор')

    def __str__(self):
        return self.title
