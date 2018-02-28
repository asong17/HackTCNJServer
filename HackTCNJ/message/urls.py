
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('postMessage/', views.post_message),

]
