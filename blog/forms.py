from django import forms
from .models import Post, Category, Comment
from django_summernote.widgets import SummernoteWidget


choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'header_image', 'subtitle',
                  'author', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add a Title'}),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add a Title tag'}),
            'subtitle': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Add a Subtitle'}),
            'author': forms.TextInput(attrs={
                'class': 'form-control', 'value': '',
                'id': 'postowner', 'type': 'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={
                'class': 'form-control'}),
            'body': SummernoteWidget(),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'subtitle', 'category', 'body')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Add a Title'}),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Add a Title tag'}),
            'subtitle': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Add a Subtitle'}),
            'category': forms.Select(choices=choice_list, attrs={
                'class': 'form-control'}),
            'body': SummernoteWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ()

        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
