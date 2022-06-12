from django.urls import path
from .views import PostView, ArticleView, AddPostView, EditPostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('post/<int:pk>', ArticleView.as_view(), name='post-detail'),
    path('add-post', AddPostView.as_view(), name='add-post'),
    path('add-category', AddCategoryView.as_view(), name='add-category'),
    path('post/edit/<int:pk>', EditPostView.as_view(), name='edit-post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete-post'),
    path('category/<str:category>/', CategoryView, name='category'),
    path('category-list', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('post/<int:pk>/comment', AddCommentView.as_view(), name='add-comment'),
]
