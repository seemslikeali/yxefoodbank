from django.shortcuts import redirect, render
from .models import Room
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here. WHERE WE CONFIGURE OUR PAGES

# from tutorial video


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    # can also be done like this return render(request, 'home.html', {'rooms': rooms})
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User doesn't exist or is deleted.")
        user = authenticate(request, username=username, password=password)

        if user != None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Username or Password is invalid.")
    context = {}
    return render(request, 'base/login.html', context)


def signup(request):
    return render(request, 'base/signup.html')
