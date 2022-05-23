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
<<<<<<< HEAD
=======
>>>>>>> d8d386a17692e349c831714aeba2a63404e7630f
=======
>>>>>>> 906a8798dc44259d798c1e3529898d0c25e3abfd
    path('', include('resultpage.urls')),
<<<<<<< HEAD
    path('', include('quiz page1.urls')),
    path('', include('quiz page2.urls')),
    path('', include('quiz page3.urls')),
    path('', include('quiz page4.urls')),
    path('', include('quiz page5.urls')),
    path('', include('quiz page6.urls')),
    path('', include('quiz page7.urls')),
    path('', include('quiz page8.urls')),
    path('', include('quiz page9.urls')),
    path('', include('quiz page10.urls')),
    path('', include('quiz page11.urls')),
    path('', include('quiz page12.urls')),

=======
    path('', include('quiz.urls')),
>>>>>>> 8d9237f3a9fb77df76f0e54668e5260bf0b6afea
]
