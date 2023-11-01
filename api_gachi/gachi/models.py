from django.db import models


class BaseName(models.Model):
    """
    Базовое полное имя.
    Связано с вариациями имени один-ко-многим
    """
    basename = models.CharField('Базовое имя', max_length=200, unique=True)
    slug = models.SlugField('Уникальный слаг', unique=True, max_length=200)

    def __str__(self):
        return self.name


class Name(models.Model):
    """
    Вариация имени.
    Связано с базовым именем и гачами один-ко-многим.
    """
    name = models.CharField('Имя', max_length=200)
    slug = models.SlugField('Уникальный слаг', unique=True, max_length=200)
    basename = models.ForeignKey(
        BaseName,
        on_delete=models.CASCADE,
        related_name='name_variants',
        verbose_name='Базовое имя',
    )

    def __str__(self):
        return self.name


class Gachi(models.Model):
    """
    Модель гачи.
    Связано с базовым именем один-ко многим
    """
    gachi = models.CharField('Гача', max_length=200)
    name = models.ForeignKey(
        Name,
        on_delete=models.CASCADE,
        related_name='gachies',
        verbose_name='Имя',
    )
    likes = models.IntegerField('Лайки', default = 0)
    dislikes = models.IntegerField('Дизлайки', default = 0)
    rating = models.IntegerField('Рейтинг', default = 0)
