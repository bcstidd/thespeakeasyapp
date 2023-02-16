from django.forms import ModelForm
from django import forms
from .models import Comment, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'language']
        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Enter translation/feedback here...'}),
        }


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['phrase', 'country_of_origin', 'native_language']
        widgets = {
            'phrase': forms.Textarea(attrs={'placeholder': 'Please enter your phrase here...'}),
            'country_of_origin': forms.TextInput(attrs={'placeholder': 'Home Country'}),
            'native_language': forms.TextInput(attrs={'placeholder': 'Native Language'}),
        }