from django.shortcuts import render, redirect
from products.models import *
from .decorators import ensure_session_key  # Импортируем декоратор

@ensure_session_key
def product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            ProductImage.objects.create(product=product, image=image, is_main=True)
            return redirect(f'http://127.0.0.1:8000/product/{product.id}/')

    print(request.session.session_key)

    return render(request, 'products/product.html', locals())
