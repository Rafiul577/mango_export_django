from django.urls import path
from . import views

urlpatterns = [
    path('', views.mango_list, name='mango_list'),
    path('create/', views.mango_create, name='mango_create'),
    path('update/<int:pk>/', views.mango_update, name='mango_update'),
    path('delete/<int:pk>/', views.mango_delete, name='mango_delete'),
]
