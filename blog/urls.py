from django.urls import path
from . import views
from .views import PostView, ArticleView, AddPostView

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('post/<int:pk>', ArticleView.as_view(), name='post-detail'),
    path('add-post', AddPostView.as_view(), name='add-post'),
]
