from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from koskas1_app.models import Product
 

def index(request):
	return render(request, "index.html")

def contact(request):
	return render(request , "contact.html")

def references(request):
	return render(request , "references.html")

def nos_prestation(request):
	products = Product.objects.all()
	return render(request , "nos_prestation.html", context={ 'products': products})


def product(request, product_id):
	product = Product.objects.get(id=product_id)
	return render(request, 'product.html', context={'product': product,})
