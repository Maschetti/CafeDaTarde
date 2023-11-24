from django.forms import ModelForm
from django import forms
from .models import User, Post


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'phone',
        ]
    
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
        ]
        
    def save(self, commit=True, user_id=None):
        instance = super().save(commit=False)
        
        if user_id is not None:
            instance.user_id = user_id
        
        if commit:
            instance.save()
    
        return instance
