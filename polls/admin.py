from django.contrib import admin
from .models import User, Post, Section, Tag

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Section)
