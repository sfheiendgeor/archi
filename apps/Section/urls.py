
from django.contrib import admin
from django.urls import path
from .views import  IndexView, upload, list, my_customized_server_error
urlpatterns = [
    path('', IndexView.as_view(), name = 'IndexView'),
    path('upload/', upload, name = 'upload'),
    path('list/', list.as_view(), name = 'list' ),
]
handler500 = my_customized_server_error