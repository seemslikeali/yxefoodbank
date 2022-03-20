from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from itertools import product
from django.shortcuts import render
from django.template import context

from account.models import Account
from store.models import Form, Formitems, Product

# Create your views here.



def userHistPage(request):
    user = request.user
    products = Product.objects.all()
    accounts = Account.objects.all()
    formitem = Formitems.objects.all()
    form = Form.objects.all()
    context = {'products':products,'account':accounts,'form': form, 'formitems':formitem}

    return render(request, 'userHist.html', context)
    


