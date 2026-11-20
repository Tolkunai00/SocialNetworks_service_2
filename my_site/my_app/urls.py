from django.urls import path
from . import views

urlpatterns = [
    path('follows/', views.FollowListView.as_view()),
    path('follows/create/', views.FollowCreateView.as_view()),
    path('follows/<int:pk>/delete/', views.FollowDeleteView.as_view()),
    path('posts/', views.PostListView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),
    path('posts/create/', views.PostCreateView.as_view()),
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view()),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view()),
    path('post-likes/create/', views.PostLikeCreateView.as_view()),
    path('post-likes/<int:pk>/delete/', views.PostLikeDeleteView.as_view()),
    path('posts/<int:post_id>/likes/', views.PostLikeListView.as_view()),
    path('comments/create/', views.CommentCreateView.as_view()),
    path('comments/<int:pk>/update/', views.CommentUpdateView.as_view()),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),
    path('comment-likes/create/', views.CommentLikeCreateView.as_view()),
    path('comment-likes/<int:pk>/delete/', views.CommentLikeDeleteView.as_view()),
    path('comments/<int:comment_id>/likes/', views.CommentLikeListView.as_view()),
]