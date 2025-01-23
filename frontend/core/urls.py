from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('administrator/', views.admin, name='administrator'),
    path('add/', views.add, name='add'),
    path('customer/', views.customer, name='customer'),
    path('buy/', views.buy, name='buy'),
]