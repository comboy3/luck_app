from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/new/',
         views.PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #     path('post/<int:pk>/comment/new/',
    #          views.CommentCreateView.as_view(), name='comment_create'),
    path('post/<int:pk>/comment/',
         views.CommentListView.as_view(), name='comment_list'),
]
