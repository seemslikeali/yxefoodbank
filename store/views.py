from inspect import _void
from itertools import product
from django.shortcuts import redirect, render
from django.template import context
from .models import Product
from .models import *
from django.http import JsonResponse


# Create your views here.


def store(request):
    products = Product.objects.all()
    context = {'products':products}
    customer = request.user
    form = Form.objects.all().filter(customer=customer).filter(complete=False)
    for x in form:
        items = x.formitems_set.all()
    context = {'products':products, 'items': items}
    return render(request, 'store.html', context)


def checkout(request):
    products = Product.objects.all()
    customer = request.user
    form = Form.objects.all().filter(customer=customer).filter(complete=False)
    for x in form:
        items = x.formitems_set.all()
    if request.method == 'POST':
        item = request.POST.get('item')
        for x in form:
            print(item)
            items = x.formitems_set.all().filter(product__name=item).delete()
            return redirect('checkout')
    context = {'products':products, 'items': items}
    return render(request, 'checkout.html', context)


def cart(request):
    print('----------------------------------->')
    print(type(request.user))
    print(request.user)
    user = request.user
    form = Form.objects.all().filter(user=user).filter(complete=False)
    for x in form:
        items = x.formitems_set.all()
        print(x.transaction_id)
        for item in items:
            print(item.quantity)
    #items = form.formitem_set.all()
    context = {'items': items}
    return render(request, 'cart.html', context)


