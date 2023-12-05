from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from PIL import Image
from .models import User, Post, Image
from .forms import UserForm, PostForm
import os

# Create your views here.
def home_view(request):
    return HttpResponse('Bem vindo ao Cafe da Tarde!')

def profile_view(request):
    user = request.user
    
    if request.method == 'POST':
        print("ENTROU")
        img = Image.objects.create(image=request.POST.get('myfile'), title='profile_pic')
        print(img)
        user.picture.image = img
        
        user.save()
    
    return render(request, 'profile.html', {'user': user})

def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ct:login')
    else:
        form = UserForm()
        
    return render(request,'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.authenticate(username, password)
        
        if user is not None:
            login(request, user)
            return redirect('ct:home')
        else:
            messages.error(request, 'Falha ao fazer login')
        
    return render(request, 'login.html')

def post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(user_id=request.user.id)
            return redirect('ct:home')
    else:
        form = PostForm()
        
    return render(request,'form.html', {'form': form})

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})
