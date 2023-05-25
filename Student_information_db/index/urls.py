from django.contrib import admin
from django.urls import path
from index import views

app_name = "index"

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.form, name='form'),

]
