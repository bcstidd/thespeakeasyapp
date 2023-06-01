from django.urls import path
from . import views
from .views import translate, about
# from userprofile.views import add_favs

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.HomeView.as_view(), name='home'),
    path('posts/', views.PostList.as_view(), name='index'),
    path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='posts_detail'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('posts/<int:post_id>/add_favs/<int:profile_id>/',views.add_favs, name='add_favs'),
    path('profiles/<int:pk>', views.ProfileDetail.as_view(), name='profile_detail'),
    path('profiles/<int:profile_id>/add_photo/', views.add_photo, name='add_photo'),
    path('translate/', translate, name='translate'),
    path('about/', about, name='about')
]
