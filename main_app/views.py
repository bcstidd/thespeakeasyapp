from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
# from django.views import TemplateView
from .models import Post, User
from userprofile.models import Profile
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


# def home(request):
#     return render(request, 'home.html')

class HomeView(TemplateView):
    user_model = User
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['profile_id'] = self.request.user.profile.id
            print("Profile below ---------------------------------")
            print(self.request.user.profile.id)
            print(context['profile_id'])
        return context

    template_name = 'home.html'


class PostList(ListView):
    model = Post


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['phrase', 'country_of_origin',
              'native_language', 'date']


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    user_model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_id'] = self.request.user.profile.id
        return context


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


def add_favs(request, profile_id, post_id):
    profile = Profile.objects.get(id=profile_id)
    post = Post.objects.get(id=post_id)
    profile.favorite_posts.add(post)
    profile.save()
    return redirect('home')


class ProfileDetail(LoginRequiredMixin, DetailView):
    model = Profile
