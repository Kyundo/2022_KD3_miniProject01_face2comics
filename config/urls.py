"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('homepage/', include('homepage.urls')),
=======
    path('', include('homepage.urls')),
<<<<<<< HEAD
=======
>>>>>>> d8d386a17692e349c831714aeba2a63404e7630f
    path('', include('resultpage.urls')),
    path('', include('quiz.urls')),

>>>>>>> e4554fe5de3e53c5aef54d7b2d3cfdfdce4a799a
]
