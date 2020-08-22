from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from django.urls import path

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home' ),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-post' ),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail' ),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update' ),
    path('post/new/', PostCreateView.as_view(), name='post-create' ),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete' ),
    path('home/', PostListView.as_view(), name='blog-home' ),
    path('about/', views.about, name='blog-about' ),
]