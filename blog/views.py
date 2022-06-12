from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class PostView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-post_date']


class ArticleView(DetailView):
    model = Post
    template_name = 'post.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add-post.html'


class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit-post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')
