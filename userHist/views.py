from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from itertools import product
from django.shortcuts import render
from django.template import context

from account.models import Account
from store.models import Customer, Form, Formitems, Product

# Create your views here.



def userHistPage(request):
    user = request.user

    # Creation of variables to call for each model
    products = Product.objects.all()
    accounts = Account.objects.all()
    formitem = Formitems.objects.all()


    form = Form.objects.all().filter(customer=user).filter(complete=True) # Specified user verification check
    context = {'products':products,'account':accounts,'form': form, 'formitems':formitem}

    # Deletion of a specified form from userHist
    if (request.method == 'POST') and ('delete' in request.POST):
        item = request.POST.get('delete')
        for x in form.filter(transaction_id = item):    # Filters through items by specified transaction_id
            x.delete()  # Deletes form model values via specified transaction_id from previous line
            return redirect('userHist') # Refreshes website with updated changes

            


    return render(request, 'userHist.html', context)
    


