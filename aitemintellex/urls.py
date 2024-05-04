from django.contrib import admin
from django.urls import path, include
from aiprouz.views import home, page_detail, blog_list, blog_detail, news_list, news_detail
urlpatterns = [
    path('', home, name='home'),  # Домашняя страница
    path('admin/', admin.site.urls),
    path('blog/', blog_list, name='blog_list'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
    path('news/', news_list, name='news_list'),
    path('news/<slug:slug>/', news_detail, name='news_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('<str:url_name>/', page_detail, name='page_detail'),
]
