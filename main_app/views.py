from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
def home(request):
  return render(request, 'home.html')

class PostList(ListView):
    model = PostList
    context_object_name = 'posts'
    template_name = 'posts/index.html'