from django.db import models
from django.urls import reverse
from datetime import date
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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_joined = models.DateTimeField()
    primary_language = models.CharField(
        max_length=2,
        choices=LANGUAGES,
        default=LANGUAGES[0][0]
    )


class Post(models.Model):
    phrase = models.TextField()
    date = models.DateTimeField()
    country_of_origin = models.CharField(max_length=200)
    native_language = models.CharField(max_length=200)
    profiles = models.ManyToManyField(Profile)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('posts_detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.id}:{self.phrase[:10]}'
