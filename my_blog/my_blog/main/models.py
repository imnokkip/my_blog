from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    slug = models.SlugField("URL-адрес", max_length=200, unique=True)
    content = models.TextField("Содержание")
    image = models.ImageField(
        "Изображение",
        upload_to='posts/',
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)
    is_published = models.BooleanField("Опубликовано", default=False)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField('Название', max_length=100)
    slug = models.SlugField('URL', max_length=100, unique=True)
    description = models.TextField('Описание')
    image = models.ImageField('Превью', upload_to='projects/')
    github_url = models.URLField('Ссылка на GitHub', blank=True)
    demo_url = models.URLField('Демо-ссылка', blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    title = models.CharField('Название', max_length=100)
    image = models.ImageField('Изображение', upload_to='gallery/')
    description = models.TextField('Описание', blank=True)
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    tags = models.CharField('Теги', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Изображение галереи'
        verbose_name_plural = 'Изображения галереи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title