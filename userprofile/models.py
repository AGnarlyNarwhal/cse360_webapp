from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_image = models.ImageField(upload_to="photos/profile_images", default="photos/profile_images/default_user.jpg",blank=True )
    
    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


