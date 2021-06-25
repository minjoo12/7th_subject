from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('new', views.new, name="new"),
    path('create', views.create, name="create"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
]