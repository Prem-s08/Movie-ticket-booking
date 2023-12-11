from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='theater-home'),
    path('nowshowing/', views.nowshowing, name='theater-nowshowing'),
    path('ticketprice/', views.ticketprice, name='theater-ticketprice'),
    path('about/', views.about, name='theater-about'),
    path('Wonka/', views.Wonka, name='Wonka'),
    path('Spiderman/', views.Spiderman, name='Spiderman'),
    path('oppenheimer/', views.oppenheimer, name='oppenheimer'),
    path('Trolls/', views.Trolls, name='Trolls'),
    path('contact/', views.contact, name='contact'),
]