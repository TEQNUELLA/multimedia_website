from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_media, name='upload_media'),
]