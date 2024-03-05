from django.urls import path
from main.views.posts import PostListGenericAPIView, CreatePostGenericAPIView, PostUpdateGenericAPIView, PostDeleteAPIView

urlpatterns = [
    path('create-post', CreatePostGenericAPIView.as_view(), name='create-post'),
    path('post-list', PostListGenericAPIView.as_view(), name='post-list'),
    path('update-post/<int:post_id>', PostUpdateGenericAPIView.as_view(), name='update-post'),
    path('delete-post/<int:post_id>', PostDeleteAPIView.as_view(), name='delete-post'),
]