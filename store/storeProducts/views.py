from django.shortcuts import render, redirect, get_object_or_404
from storeProducts.models import Product, ProductCategory, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def index(request):
    context = {
        'title' : 'alina store products home',
        'welcome_message' : 'welcome to the 1-23 store!',
        'products': Product.objects.all(),              
        'categories': ProductCategory.objects.all()      
    }
    return render(request, 'storeProducts/index.html', context)

def products(request, category_id=None, page_number=1): 
    products_queryset = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 3
    paginator = Paginator(products_queryset, per_page)
    products_paginator = paginator.page(page_number)
    if category_id:
        current_category = ProductCategory.objects.get(id=category_id)
        title = f'alina store products catalog - {current_category.name}' 
    else:
        title = 'alina store products catalog'
        current_category = None

    context = {
        'title': title, 
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,             
        'current_category': current_category,
    }
    
    return render(request, 'storeProducts/products.html', context)
  
@login_required    
def basket_add(request, product_id):
  product = Product.objects.get(id=product_id)
  baskets = Basket.objects.filter(user=request.user, product=product)
  
  if not baskets.exists():
    Basket.objects.create(user=request.user, product=product, quantity=1)
  else:
    basket = baskets.first()
    basket.quantity += 1
    basket.save()
    
  
  return redirect(request.META['HTTP_REFERER'])

@login_required 
def basket_remove(request, basket_id):
  basket = Basket.objects.get(id=basket_id)
  basket.delete()
  return redirect(request.META['HTTP_REFERER'])