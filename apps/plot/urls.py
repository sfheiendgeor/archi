
from django.contrib import admin
from django.urls import path
from .views import index, WallPlot

urlpatterns = [
    path("", index, name = "plot"),
    path("wall/",WallPlot.as_view(), name = 'WallPlot')
]
