from django.shortcuts import render
from .forms import SubscriberForm
from products.models import *


def landing(request):
    name = "baklan"
    current_day = "05.05.2024"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_new = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)[:8]
    products_images_bread = products_images.filter(product__category__id=1)
    products_images_vegetables = products_images.filter(product__category__id=2)
    products_images_meat = products_images.filter(product__category__id=3)
    products_images_pelmeni = products_images.filter(product__category__id=4)
    products_images_souses = products_images.filter(product__category__id=5)
    products_images_juices = products_images.filter(product__category__id=6)
    products_images_milks = products_images.filter(product__category__id=7)
    return render(request, 'landing/home.html', locals())


def aboutUs(request):
    return render(request, 'landing/aboutUs.html')
