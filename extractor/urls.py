from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
]