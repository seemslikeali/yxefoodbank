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
<<<<<<< Updated upstream
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
=======
    form, created = Form.objects.get_or_create(customer=customer, complete=False)
    if (form.transaction_id == None):
        formnum = Formmetrics.objects.all()

        #form.transaction_id = 23
        #print(form.transaction_id)
        print(formnum)

    items = form.formitems_set.all()


    if (request.method == 'POST') and ('delete' in request.POST):
        item = request.POST.get('delete')
        form.formitems_set.all().filter(product__name=item).delete()
        return redirect('store')

    
    if (request.method == 'POST') and ('add' in request.POST):
        item = request.POST.get('add')
        product_added = Product.objects.get(name=item)
        data = form.formitems_set.all().filter(product__name=item)
        if data.count() == 0:
            form.formitems_set.create(
                    product = product_added,
                    form = form,
            )
            return redirect('store')



    if (request.method == 'POST') and ('submit' in request.POST):
        item = request.POST.get('submit')
        form.complete = True
        return redirect('store')
>>>>>>> Stashed changes


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


