from django.urls import path, include
from .views import *

urlpatterns = [
    path('welcome/', welcome, name='welcome'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('tracking/', tracking, name='tracking'),
    path('', home, name='home'),
    path('features/', features, name='features'),
    path('dashboard/', dashboard, name='dashboard'),

]