from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list, name='posts_list'),
    # path('post/<str:slug>/', post_detail, name='post_detail'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('tags/', tags_list, name='tags_list'),
    path('tag/<str:slug>/', tag_detail, name='tag_detail'),
]
