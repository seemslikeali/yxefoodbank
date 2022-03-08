from itertools import product
from django.shortcuts import render
from django.template import context
from .models import Product

# Create your views here.


def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store.html', context)


