from django.shortcuts import render
from store.models import Product, Category
from django.shortcuts import get_object_or_404, render


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def list_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products':products })


def product_detail(request,slug):
     product = get_object_or_404(Product, slug=slug, in_stock=True)
     return render(request, 'store/detail.html', {'product': product})

def list_categories(request, cat_slug):
    category= get_object_or_404(Category, slug=cat_slug )
    products = Product.objects.filter(category= category)
    return render(request, 'store/category.html', {'category': category, 'products':products})