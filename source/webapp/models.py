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


class Comment(models.Model):
    commented_to = models.OneToOneField(Article, on_delete=models.CASCADE, null=True,
                                        related_name='comment_to', verbose_name='Комментарий к статье', blank=True)
    comment = models.TextField(max_length=1000, blank=True, verbose_name='Комментарий')
    commented_by = models.OneToOneField(User, related_name='comment', on_delete=models.CASCADE,
                                        verbose_name='Комментарий пользователя')
    comment_to_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name='commented_comment',
                                           verbose_name='Комментарий к комментарию', blank=True, null=True)

    def __str__(self):
        return self.comment

