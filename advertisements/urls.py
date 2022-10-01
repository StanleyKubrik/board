from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('advertisement', views.advertisement_prices, name='advertisement_prices'),
    path('about', views.About.as_view(), name='about')
]
