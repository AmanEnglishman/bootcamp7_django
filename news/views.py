from django.shortcuts import render
from django.db.models import Q

from .models import News

def home(request):
    query = request.GET.get('q')

    if query:
        news = News.objects.filter(
            Q(title__icontains=query) |
            Q(short_description__icontains=query)
        ).order_by('-created_at')
    else:
        news = News.objects.all().order_by('-created_at')

    return render(request, 'index.html', {'news': news, 'query': query})

'''
http://127.0.0.1:8000/?q=
'''

def contacts(request):
    return render(request, 'contacts.html')

def news_detail(request, pk):
    news = News.objects.get(pk=pk)
    return render(request, 'news_detail.html', context={'news': news})
