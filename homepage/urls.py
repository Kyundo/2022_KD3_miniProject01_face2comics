from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('homepage/', views.homepage),
    path('index/', views.index),
    path('gallery/', views.gallery),
    path('contact/', views.contact),
<<<<<<< HEAD
    path('upload2/', views.upload2, name='upload2'),
    path('upload3/', views.upload3, name='upload3'),
    path('download/', views.download, name='download'),
    path('index1/', views.index1),
    path('test/',views.test),
    path('upload/',views.upload),
=======
<<<<<<< HEAD
    path('upload1/', views.upload1, name='upload1'),
    path('upload2/', views.upload2, name='upload2'),
    path('upload3/', views.upload3, name='upload3'),
    
    path('download/', views.download, name='download'),
=======
    path('index1/', views.index1),
    path('test/',views.test),
    path('upload/',views.upload),

>>>>>>> d8d386a17692e349c831714aeba2a63404e7630f
>>>>>>> 11bc1c57d4322e8515c100fd3a3d8d448b7fdb00
]