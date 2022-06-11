from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'subtitle', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a Title tag'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a Subtitle'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Start blogging...'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'subtitle', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a Title tag'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a Subtitle'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Start blogging...'}),
        }