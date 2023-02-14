# from django.shortcuts import render, redirect
# from .models import Profile
# from main_app.models import Post


# def add_favs(request, profile_id, post_id):
#     profile = Profile.objects.get(id=profile_id)
#     post = Post.objects.get(id=post_id)
#     profile.favorite_posts.add(post)
#     profile.save()
#     return redirect('details')
