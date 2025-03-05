from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),   
    path('services', views.services, name='services'),  
    path('contact', views.contact, name='contact'),
    path('agreement', views.agreement, name='agreement'),
    path('support', views.support, name='support'),
    path('career', views.career, name='career'),
    path('performance', views.performance, name='performance'),
    path('incident', views.incident, name='incident'),
    path('microlearning', views.microlearning, name='microlearning'),
    path('ergonomic', views.ergonomic, name='ergonomic'),
]