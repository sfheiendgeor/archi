
from django.contrib import admin
from django.urls import path
from .views import  GlassdesignView

urlpatterns = [
    path('', GlassdesignView.as_view(), name = 'GlassdesignView'),
]
