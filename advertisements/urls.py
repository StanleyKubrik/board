from django.urls import path
from . import views

urlpatterns = [
    path('', views.Advertisement.as_view(), name='advertisement_list'),
    path('advertisement', views.advertisement_prices, name='advertisement_prices'),
    path('contacts', views.Contacts.as_view(template_name='advertisements/about.html'), name='contacts'),
    path('about', views.About.as_view(template_name='advertisements/about.html'), name='about'),
]
