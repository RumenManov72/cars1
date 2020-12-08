from django.urls import path

from accounts.views import register, login, dashboard, logout
from cars.views import cars, car_detail, search

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]