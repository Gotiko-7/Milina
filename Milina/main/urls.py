from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('wedo', views.wedo, name='wedo'),
    path('pricing', views.pricing, name='pricing'),
    path('contact', views.contact, name='contact'),
    path('readmore', views.readmore, name='readmore'),
    path('experts', views.experts, name='experts'),
]