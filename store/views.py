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


    if (request.method == 'POST') and ('delete' in request.POST):
        item = request.POST.get('delete')
        for x in form:
            x.formitems_set.all().filter(product__name=item).delete()
            return redirect('store')

    
    if (request.method == 'POST') and ('add' in request.POST):
        item = request.POST.get('add')
        product_added = Product.objects.get(name=item)
        for x in form:
            data = x.formitems_set.all().filter(product__name=item) 
            if data.count() == 0:
                x.formitems_set.create(
                        product = product_added,
                        form = form,
                )
                return redirect('store')



    if (request.method == 'POST') and ('submit' in request.POST):
        item = request.POST.get('submit')
        for x in form:
            x.complete = True
            return redirect('store')



    context = {'products':products, 'items': items}
    return render(request, 'store.html', context)

