from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('post-detail/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('create-post/', views.PostCreateView.as_view(), name='create-post'),
    path('posts/<str:pk>/', views.UserPostListView.as_view(), name='user-post-list'),
    path('post/reaction/', views.post_reaction, name='post-reaction'),
    path('post/comment/reaction/', views.post_comment_reaction, name='post-comment-reaction')
]