from django.urls import path


from .views import home, contacts, news_detail

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/', news_detail, name='news_detail'),
]
