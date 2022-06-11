from django.urls import path
from . import views
from .views import PostView, ArticleView, AddPostView, EditPostView, DeletePostView

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('post/<int:pk>', ArticleView.as_view(), name='post-detail'),
    path('add-post', AddPostView.as_view(), name='add-post'),
    path('post/edit/<int:pk>', EditPostView.as_view(), name='edit-post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
]
