# Generated by Django 2.0.9 on 2018-12-16 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_article_marked_by_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='marked_by_user',
        ),
    ]
