from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.PostList.as_view(), name='index'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='posts_detail'),
    path('accounts/signup/', views.signup, name='signup'),
]