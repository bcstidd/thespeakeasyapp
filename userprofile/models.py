from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from main_app.models import Post
# Create your models here.
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
    primary_language = models.CharField(
        max_length=20,
        choices=LANGUAGES,
        default=LANGUAGES[2][1],
        null=True
    ),
    favorite_posts = models.ManyToManyField(
        Post, related_name='favorited_by', blank=True)

    def __str__(self):
        return f'{self.id}:{self.user.username}, {self.get_primary_language_display()}, {self.favorite_posts}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
