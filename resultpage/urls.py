from django.urls import path
from . import views

app_name = 'resultpage'

urlpatterns = [
    path('resultpage/', views.resultpage),
]