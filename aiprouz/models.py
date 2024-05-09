# aitemintellex/aiprouz/models.py
import os
from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.utils.translation import gettext as _
from django.urls import reverse
from django_quill.fields import QuillField

class ExternalNews(models.Model):
    topic = models.CharField(max_length=200, verbose_name="Тема")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(verbose_name="Описание")
    content = QuillField(verbose_name="Содержимое")
    source_url = models.URLField(max_length=500, verbose_name="Ссылка на источник")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Внешняя новость"
        verbose_name_plural = "Внешние новости"
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(ExternalNews, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})

class DailyReport(models.Model):
    content = models.CharField(max_length=200, verbose_name="Content")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Created at")

    def __str__(self):
        return f"Report for {self.created_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Daily report"
        verbose_name_plural = "Daily repots"

# для создания страниц из админки
def get_template_choices():
    templates_dir = os.path.join(settings.BASE_DIR, 'aiprouz', 'templates')
    templates_files = os.listdir(templates_dir)
    return [(template, template) for template in templates_files if template.endswith('.html')]

class Page(models.Model):
    PAGE_CHOICES = [
        ('team', 'Team'),
        ('service', 'Service'),
        ('interesting', 'Interesting'),
        ('events', 'Events'),
        ('blog', 'Blog'),
        ('trading', 'Trading')
    ]

    url_name = models.CharField(max_length=50, unique=True, choices=PAGE_CHOICES)
    template_name = models.CharField(max_length=100, choices=get_template_choices())
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    content = QuillField()
    last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'url_name': self.url_name})
# Отдельно для блогов
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    content = QuillField() # <--- Ошибка здесь
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def get_absolute_url(self):
        if self.slug:  # Проверяем, что slug существует
            return reverse('blog_detail', args=[self.slug])
        else:
            return "#"  # Возвращаем placeholder, если slug пустой
