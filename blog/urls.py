from django.urls import path, include, re_path  # Import re_path here

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)

from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    # path('post/<int:pk>/like/', like_post ,name='like-post'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='contact'),
    path('howitworks/', views.howitworks, name='howitworks'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
]
