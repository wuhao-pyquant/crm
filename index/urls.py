from django.urls import path
from .views import  *

app_name = 'index'
urlpatterns = [
    path('index/', index, name='index'),
    path('main/', main, name='main'),
]