from django.shortcuts import render
from .models import News

def home(request):
    news = News.objects.all()
    return render(request, 'index.html', context={'news': news})

def contacts(request):
    return render(request, 'contacts.html')

def news_detail(request, pk):
    news = News.objects.get(pk=pk)
    return render(request, 'news_detail.html', context={'news': news})
