from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from account.forms import RegistrationForm
# Create your views here.


def registration_view(request):
    # when user is already signed in, they shouldn't be allowed in sign up page
    if request.user.is_authenticated:
        return redirect('/')

    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            print("didnt work")
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)
