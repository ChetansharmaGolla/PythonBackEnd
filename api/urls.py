from django.urls import path
from . import views

urlpatterns = [
    path('/v1/getstations', views.home, name='home'),
    path('', views.home),
]
