from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('administrator/', views.admin, name='administrator'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('customer/', views.customer, name='customer'),
    path('buy/<int:id>', views.buy, name='buy'),
]