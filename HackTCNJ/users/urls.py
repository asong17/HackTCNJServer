
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('loginStudent/', views.login_student),
    path('seeMessages/', views.see_unapproved),
    path('loginAdmin/', views.login_admin),
    path('approveMessage/', views.approve_message)

]
