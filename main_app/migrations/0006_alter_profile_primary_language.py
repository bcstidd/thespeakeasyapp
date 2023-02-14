# Generated by Django 4.1.6 on 2023-02-13 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_profile_primary_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='primary_language',
            field=models.CharField(choices=[('ZH', '中文'), ('ES', 'Español'), ('EN', 'English'), ('HI', 'हिन्दी-उर्दू'), ('AR', 'العربية'), ('BN', 'বাংলা'), ('PT', 'Português'), ('RU', 'Русский'), ('FR', 'Français'), ('HE', 'עברית')], default='English', max_length=20, null=True),
        ),
    ]