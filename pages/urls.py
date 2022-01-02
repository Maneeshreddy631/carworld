from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'), #about is name of url
    path('services', views.services, name='services'), #services is name of url
    path('contact', views.contact, name='contact'),
]
