from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('homepage/', views.homepage),
    path('index/', views.index),
    path('gallery/', views.gallery),
    path('contact/', views.contact),
    path('upload1/', views.upload1, name='upload1'),
    path('upload2/', views.upload2, name='upload2'),
    path('upload3/', views.upload3, name='upload3'),
    
    path('download/', views.download, name='download'),
]