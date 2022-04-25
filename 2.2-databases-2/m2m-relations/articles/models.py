from django.db import models


class Tag(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Tag, related_name='articles', through='ArticleTag')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class ArticleTag(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='tag')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Раздел', related_name='tag')
    is_main = models.BooleanField(verbose_name='Основной', blank=True)

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статьи'