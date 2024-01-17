from django.urls import path
from .views import *

app_name = 'ideas'

urlpatterns = [
    path('',list, name='list'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('toggle_favorite/', toggle_favorite, name='toggle_favorite'),
    path('change_interest/', change_interest, name='change_interest'),
    path('update/<int:pk>/',update, name='update'),
    path('delete/<int:pk>', delete, name='delete'),
]
