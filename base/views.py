from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Using login required all you have to do is write @login_required line before function
# Create your views here. WHERE WE CONFIGURE OUR PAGES


def home(request):
    # can also be done like this return render(request, 'home.html', {'rooms': rooms})
    return render(request, 'base/home.html')


def volunteerPage(request):
    return render(request, 'base/volunteer.html')


def aboutPage(request):
    return render(request, 'base/about.html')


# recently added volunteer form view
def volunteerFormPage(request):
    return render(request, 'base/volunteerform.html')


def contactPage(request):
    return render(request, 'base/contact.html')


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
            messages_in_django = messages.get_messages(request)
            for message in messages_in_django:
                pass
            return redirect('/')
        else:
            messages.error(request, "Username or Password is invalid.")
    context = {}
    return render(request, 'base/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')
