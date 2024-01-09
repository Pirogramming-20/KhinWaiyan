from django.urls import path
from .views import *

app_name = 'demos'

urlpatterns = [
    # view 에 있는 function 인 index 연결
    path('index/', index, name='index'),
    path('calculator/', calculator, name='calculator'),
]