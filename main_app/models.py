from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Post(models.Model):
    phrase = models.TextField()
    date = models.DateTimeField()
    country_of_origin = models.CharField(max_length=200)
    native_language = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.id}:{self.phrase[:10]}'


