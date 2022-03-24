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
    customer = request.user
    # if form doesnt exist create a new one
    form, created = Form.objects.get_or_create(
        customer=customer, complete=False)
    # If form is new, form ID is created using the Item ID
    if (form.transaction_id == None):
        Form.objects.all().filter(customer=customer,
                                  complete=False).update(transaction_id=form.id)
    items = form.formitems_set.all()

    # if POST is received with delete (button is pressed), associated object deleted
    if (request.method == 'POST') and ('delete' in request.POST):
        item = request.POST.get('delete')
        form.formitems_set.all().filter(product__name=item).delete()
        return redirect('store')

    # if POST is received with add (button is pressed), associated object added
    if (request.method == 'POST') and ('add' in request.POST):
        item = request.POST.get('add')
        product_added = Product.objects.get(name=item)
        data = form.formitems_set.all().filter(product__name=item)
        if data.count() == 0:
            form.formitems_set.create(
                product=product_added,
                form=form,
            )
            return redirect('store')

    # if POST is received with submit (button is pressed), form is submitted.
    if (request.method == 'POST') and ('submit' in request.POST):
        Form.objects.all().filter(customer=customer, complete=False).update(complete=True)
        return redirect('store')

    context = {'products': products, 'items': items}
    return render(request, 'store.html', context)
