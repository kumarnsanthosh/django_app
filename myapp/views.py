from django.shortcuts import render
from .models import Group, Product
# Create your views here.


def home(request):
    all_p = Group.objects.all()
    return render(request, 'home.html', {'products': all_p})

def products(request, id):
    pro = Product.objects.filter(category=id)
    return render(request, 'products.html', {'pro':pro})

def pdetails(request, id):
    pro = Product.objects.get(id=id)
    return render(request, 'pdetails.html', {'pro':pro})