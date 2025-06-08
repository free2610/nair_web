from django.shortcuts import redirect, render
from .models import *
from .forms import *
import random
import numpy as np

# Create your views here.
def home(requests):
    ctg = Category.objects.all()
    advertising=Advertising.objects.all()
    sneaker = Sneakers.objects.all()
    random_sneak = random.choice(advertising)
    ctx = {
        'ctg': ctg,
        'sneaker':sneaker,
        'random_sneak':random_sneak,
    }
    return render(requests, 'blog/index.html',ctx)
def contact(requests):
    ctg = Category.objects.all()
    form = ContactForm()
    if  requests.POST:
        forms=ContactForm(requests.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')

    ctx = {'ctg':ctg}
    return render(requests, 'blog/contact.html',ctx)
def register(requests):
    ctg = Category.objects.all()
    form = RegisterForm()
    if  requests.POST:
        forms=RegisterForm(requests.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    ctx = {'ctg':ctg}
    return render(requests, 'blog/register.html',ctx)
def single(requests,pk=None):
    ctg = Category.objects.all()
    sneakers = Sneakers.objects.all()
    random_s = np.random.choice(sneakers, size=3,replace=False)
    products_pk = Sneakers.objects.get(pk=pk)
    form = ChoicesForm()
    if  requests.POST:
        forms=ChoicesForm(requests.POST or  None,
                          requests.FILES or None)
        if forms.is_valid():
            root = forms.save()
            root = Buy.objects.get(pk=root.id)
            root.product = products_pk
            root.save()
            return redirect('home')
        else:
            print(forms.errors)
    ctx = {
        'ctg':ctg,
        'product_pk':products_pk,
        'form':form,
        'random_s':random_s,
        'sneakers':sneakers,
    }
    return render(requests, 'blog/single.html',ctx)
def products(requests, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)
    sneaker= Sneakers.objects.all().filter(type_id=category.id)
    ctx = {
        'ctg':ctg,
        'category':category,
        'sneaker': sneaker,
    }
    return render(requests, 'blog/products.html',ctx)