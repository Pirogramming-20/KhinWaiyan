from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'main'

urlpatterns = [
    path('home/', home, name='home'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', signup, name='signup'),
    path('toggle_like/', toggle_like, name='toggle_like'),
    path('add_comment/', add_comment, name='add_comment'),
    path('delete_comment/', delete_comment, name='delete_comment'),
    path('create_post/', create_post, name='create_post'),
    path('delete_post/', delete_post, name='delete_post'),
]
