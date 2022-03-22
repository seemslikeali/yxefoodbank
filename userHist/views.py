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
    products = Product.objects.all()
    accounts = Account.objects.all()
    form = Form.objects.all().filter(customer=user).filter(complete=True)
    formitem = Formitems.objects.all()
    context = {'products':products,'account':accounts,'form': form, 'formitems':formitem}


    return render(request, 'userHist.html', context)
    
def deleteForm(request,transaction_id):
    forms = Form.objects.all().filter(transaction_id = transaction_id)
    forms.delete()
    return redirect('delete')



