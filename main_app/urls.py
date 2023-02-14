from django.urls import path
from . import views
from userprofile.views import add_favs

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.PostList.as_view(), name='index'),
    path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='posts_detail'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('add-favs/', add_favs, name='add_favs'),

]
