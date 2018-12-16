# Generated by Django 2.0.9 on 2018-12-16 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20181216_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.CharField(choices=[('perfectly', 'Отлично'), ('good', 'Хорошо'), ('normally', 'Нормально'), ('bad', 'Плохо'), ('horrible', 'Ужасно')], max_length=30, verbose_name='Оценка'),
        ),
    ]
