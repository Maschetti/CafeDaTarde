from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import SiteUser

# Create your views here.

def index(request):
    return HttpResponse("Hello World.")

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        number = request.POST['number']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        user = User.objects.create_user(username, email, password, first_name, last_name)
        
        if user is not None:
            SiteUser.objects.create(user=user, number=number, email=email)
            return redirect('ct:index')
        
        else:
            message.error(request, 'Não foi possível cadastrar o usuário.')
    return  render(request, 'register_template.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('site_anb:index')

        else:
            messages.error(request, 'Apelido ou senha incorretos.')
    return render(request, 'site_anb/login_template.html')
