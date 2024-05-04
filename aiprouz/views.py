from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext
from aiprouz.models import Page, BlogPost, ExternalNews
from django.core.paginator import Paginator
def home(request):
    return render(request, 'home.html')

def page_detail(request, url_name):
    page = get_object_or_404(Page, url_name=url_name)
    return render(request, page.template_name, {'page': page})
def blog_list(request):
    posts = BlogPost.objects.all().order_by('-published_date')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog_list.html', {'page_obj': page_obj})
def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/blog_detail.html', {'post': post})
def news_list(request):
    news = ExternalNews.objects.all()[:15]
    return render(request, 'news_list.html', {'news': news})

def news_detail(request, slug):
    news_item = get_object_or_404(ExternalNews, slug=slug)
    return render(request, 'news_detail.html', {'news_item': news_item})
