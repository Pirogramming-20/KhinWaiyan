from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('<int:pk>/', views.review_detail, name='review_detail'),
    path('create/', views.review_create, name='review_create'),
    path('edit/<int:pk>/', views.review_edit, name='review_edit'),
    path('delete/<int:pk>/', views.review_delete, name='review_delete'),

]