import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
# from django.views import TemplateView
from .models import Post, User
from userprofile.models import Profile, Photo
from .forms import CommentForm, UserForm


from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['profile_id'] = self.request.user.profile.id
        return context


class PostList(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['profile_id'] = self.request.user.profile.id
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['phrase', 'country_of_origin',
              'native_language', 'date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['profile_id'] = self.request.user.profile.id
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['profile_id'] = self.request.user.profile.id
        return context


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['profile_id'] = self.request.user.profile.id
        return context


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # user.email = form.cleaned_data['email']
            # user.first_name = form.cleaned_data['first_name']
            # user.last_name = form.cleaned_data['last_name']
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class ProfileDetail(LoginRequiredMixin, DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['profile_id'] = self.request.user.profile.id
        return context


def add_favs(request, profile_id, post_id):
    profile = Profile.objects.get(id=profile_id)
    post = Post.objects.get(id=post_id)
    profile.favorite_posts.add(post)
    profile.save()
    return redirect('home')


def add_photo(request, profile_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            # build the full url string
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            # we can assign to profile_id or profile (if you have a profile)
            Photo.objects.create(url=url, profile_id=profile_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('profile_detail', pk=profile_id)
