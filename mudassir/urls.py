from django.urls import path
from mudassir import views

urlpatterns = [
    path('', views.welcome),
    path('create/', views.create),
    path('add/', views.add),
    path('show/', views.show),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
]