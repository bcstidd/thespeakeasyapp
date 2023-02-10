from django.db import models
from datetime import date

class Post(models.Model):
    phrase = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    country_of_origin = models.CharField(max_length=200)
    native_language = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id}:{self.phrase[:10]}'