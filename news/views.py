from django.shortcuts import render
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings

from .models import News, Category
from .forms import ContactForm

def home(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')

    news = News.objects.all().order_by('-created_at')

    if query:
        news = news.filter(
            Q(title__icontains=query) |
            Q(short_description__icontains=query)
        )

    if category_id:
        news = news.filter(category_id=category_id)

    categories = Category.objects.all()

    return render(request, 'index.html', {
        'news': news,
        'query': query,
        'categories': categories,
        'active_category': int(category_id) if category_id else None
    })




def contacts(request):
    sent = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message = f"""
                    Имя: {name}
                    Email: {email}
                    Сообщение:
                    {message}
                    """
            send_mail(
                subject="От okurmen news",
                message=full_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER,],
                fail_silently=False,
            )

            sent = True
    else:
        form = ContactForm()

    return render(request, "contacts.html", {"form": form, "sent": sent})


def news_detail(request, pk):
    news = News.objects.get(pk=pk)
    return render(request, 'news_detail.html', context={'news': news})

