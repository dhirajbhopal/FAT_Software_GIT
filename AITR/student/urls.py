from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('insert', views.insert),
    path('empfatdata', views.empfatdata),
    path('new', views.new),
    path('upload', views.upload),
    path('qr', views.insertqr),
    path('insertqr', views.insertqr),
    path('updateqr', views.updateqr),
    path('', views.all),
    path('rawall', views.rawall),
   ]
