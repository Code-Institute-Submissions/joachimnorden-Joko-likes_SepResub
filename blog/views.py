from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class PostView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class ArticleView(DetailView):
    model = Post
    template_name = 'post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


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


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category-list.html', {'cat_menu_list':cat_menu_list})


def CategoryView(request, category):
    category_posts = Post.objects.filter(category=category.replace('-', ' '))
    return render(request, 'categories.html', {'category':category.title().replace('-', ' '), 'category_posts':category_posts})

