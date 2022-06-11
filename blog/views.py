from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


class PostView(ListView):
    model = Post
    template_name = 'index.html'


class ArticleView(DetailView):
    model = Post
    template_name = 'post.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add-post.html'
