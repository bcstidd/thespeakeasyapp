from django.forms import ModelForm
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'language']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']