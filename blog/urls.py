from django.urls import path
from .views import BlogView, PostDetails, AddPost, EditPost, DeletePost


urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('post/<int:pk>', PostDetails.as_view(), name='post_details'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('post/edit/<int:pk>', EditPost.as_view(), name='edit_post'),
    path('post/<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
]
