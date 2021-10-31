from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('post/<str:slug>/', posts_detail, name='post_detail'),
]
