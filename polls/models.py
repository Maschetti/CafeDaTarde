from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Image(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=20)
    
class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_journalist = models.BooleanField(default=False)
    picture = models.OneToOneField(Image, on_delete=models.SET_NULL, null=True, blank=True)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.OneToOneField(Image, on_delete=models.SET_NULL, null=True, blank=True)
    user_id = models.PositiveIntegerField()
    pub_date = models.DateField(default=timezone.now)
    