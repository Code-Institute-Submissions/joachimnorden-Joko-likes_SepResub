from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
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


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add-category.html'
    fields = '__all__'    


class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit-post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')


def CategoryView(request, category):
    category_posts = Post.objects.filter(category=category.replace('-', ' '))
    return render(request, 'categories.html', {'category':category.title().replace('-', ' '), 'category_posts':category_posts})

