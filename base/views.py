from django.shortcuts import redirect, render
from .models import Room
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .sforms import SignupForm
# Using login required all you have to do is write @login_required line before function


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
    # if a user is logged in, they can't login again
    if request.user.is_authenticated:
        return redirect('/')

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


def logoutUser(request):
    logout(request)
    return redirect('/')


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log the user in auto with theline of code below
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Succesful"))
            return redirect('/')
    else:
        form = SignupForm()
    return render (request, 'base/signup.html', {'form':form})