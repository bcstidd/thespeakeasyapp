from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Post
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

class PostList(ListView):
    model = Post

class PostCreate(CreateView):
    model = Post
    fields = ['phrase', 'country_of_origin', 'native_language', 'date']

    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)

class PostDetail(DetailView):
    model = Post

class PostUpdate(UpdateView):
  model = Post
  fields = ['phrase', 'country_of_origin', 'native_language', 'date']

class PostDelete(DeleteView):
  model = Post
  success_url = '/posts'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)