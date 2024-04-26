from django.contrib import admin
from django.urls import path
from aiprouz.views import home  # Импортируем функцию view, созданную ранее
urlpatterns = [
    path('', home, name='home'),  # Домашняя страница
    path('admin/', admin.site.urls),
]
