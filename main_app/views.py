from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Post, Profile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def home(request):
    return render(request, 'home.html')


class PostList(ListView):
    model = Post


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['phrase', 'country_of_origin', 'native_language', 'date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post, Profile


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['phrase', 'country_of_origin', 'native_language', 'date']


class PostDelete(LoginRequiredMixin, DeleteView):
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


@login_required
def add_favs(request, post_id, profile_id):
    Post.objects.get(id=post_id).profiles.add(profile_id)
    return redirect('detail', post_id=post_id)
