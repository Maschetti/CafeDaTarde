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
    
    def authenticate(username, password):
        user = User.objects.get(username=username)
        if user.password == password:
            return user
        return None
    
class Section(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=60)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name 

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.OneToOneField(Image, on_delete=models.SET_NULL, null=True, blank=True)
    user_id = models.PositiveIntegerField()
    pub_date = models.DateField(default=timezone.now)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
        
    def __str__(self):
        return self.title
        