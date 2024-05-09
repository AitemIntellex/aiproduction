# aitemintellex/aiprouz/admin.py
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.urls import reverse
from django_quill.fields import QuillField
from django_quill.widgets import QuillWidget
from aiprouz.models import (
    DailyReport, Page, BlogPost, ExternalNews
)
@admin.register(ExternalNews)
class ExternalNewsAdmin(admin.ModelAdmin):
    list_display = ('topic', 'title', 'source_url')
    list_filter = ('topic',)
    search_fields = ('title', 'description', 'content')
    fields = ('topic', 'title', 'description', 'content', 'source_url')

@admin.register(DailyReport)
class DailyReportAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'content')
    fields = ('content',)
    readonly_fields = ('created_at',)

    def save_model(self, request, obj, form, change):
        obj.created_at = timezone.now()  # Устанавливаем текущее время
        super().save_model(request, obj, form, change)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'view_blog_link', 'view_all_blogs_link')
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'content')
    formfield_overrides = {
        QuillField: {'widget': QuillWidget}
    }

    def view_blog_link(self, obj):
        url = obj.get_absolute_url()
        return format_html("<a href='{}' target='_blank'>View Blog</a>", url)
        return "No URL available"  # Если slug не установлен

    def view_all_blogs_link(self, obj):
        url = reverse('blog_list')
        return format_html("<a href='{}' target='_blank'>View All Blogs</a>", url)
    view_all_blogs_link.short_description = "All Blog Posts"
    view_blog_link.short_description = "View Blog"

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_link', 'last_edited')
    list_filter = ['last_edited']
    search_fields = ['title', 'description', 'content']
    fields = ('url_name', 'template_name', 'title', 'description', 'content')

    def url_link(self, obj):
        return format_html("<a href='{}' target='_blank'>{}</a>", obj.get_absolute_url(), obj.url_name)
    url_link.short_description = "URL Name"  # Название колонки в админке
