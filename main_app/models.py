from django.db import models
from django.urls import reverse
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User


LANGUAGES = (
    ('ZH', '中文'),  # Mandarin Chinese
    ('ES', 'Español'),  # Spanish
    ('EN', 'English'),  # English
    ('HI', 'हिन्दी-उर्दू'),  # Hindi-Urdu
    ('AR', 'العربية'),  # Arabic
    ('BN', 'বাংলা'),  # Bengali
    ('PT', 'Português'),  # Portuguese
    ('RU', 'Русский'),  # Russian
    ('FR', 'Français'),  # French
    ('HE', 'עברית'),  # Hebrew
)


class Post(models.Model):
    phrase = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    country_of_origin = models.CharField(max_length=200)
    native_language = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.id}:{self.phrase[:10]}'


class Comment(models.Model):
    comment = models.TextField(max_length=500)
    date = models.DateField(default=timezone.now)
    language = models.CharField(
        max_length=20,
        choices=LANGUAGES,
        default=LANGUAGES[2][0],
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}:{self.comment[:10]}'

    class Meta:
        ordering = ['-date']

