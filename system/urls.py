from django.urls import path
from .views import  *

app_name = 'system'
urlpatterns = [
    path('login/', login, name='login'),

]