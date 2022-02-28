from django.shortcuts import render
from .models import Room
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


def login(request):
    return render(request, 'base/login.html')


def signup(request):
    return render(request, 'base/signup.html')
