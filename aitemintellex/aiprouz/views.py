'''Этот модуль собирает вспомогательные функции и классы,
которые «охватывают» несколько уровней MVC.
Другими словами, эти функции/классы для удобства вводят контролируемую связь.'''
from django.shortcuts import render
from django.utils.translation import gettext

def home(request):
    return render(request, 'home.html')
