from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from PIL import Image
from .models import User, Post
from .forms import UserForm, PostForm
import os

# Create your views here.
def home_view(request):
    return HttpResponse('Bem vindo ao Cafe da Tarde!')

def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ct:home')
    else:
        form = UserForm()
        
    return render(request,'form.html', {'form': form})

def post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(user_id=request.user.id)
            return redirect('ct:home')
    else:
        form = PostForm()
        
    return render(request,'form.html', {'form': form})
