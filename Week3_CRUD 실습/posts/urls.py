from django.urls import path,include
from .views import *

urlpatterns = [
    path("",posts_list),
    path("<int:pk>",posts_read),
    path("create",posts_create),
    # path("create_final",posts_create_final),
]
