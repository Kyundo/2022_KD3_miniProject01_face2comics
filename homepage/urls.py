from django.urls import path
from . import views

app_name = 'homepage'

urlpatterns = [
    path('homepage/', views.homepage),
    path('index/', views.index),
    path('gallery/', views.gallery),
    path('contact/', views.contact),
    path('index1/', views.index1),
    path('test/',views.test),
    path('upload/',views.upload),

]