from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import userProfile
from django.contrib import messages
from .models import Product
from order.models import Order

# Create your views here.

# products
@login_required(login_url='signin')
def products(request):
    ContentCart=Order.objects.filter(user=request.user, is_delivered=False).count()
    user=userProfile.objects.get(userInfo=request.user)
    numCoffee=user.favoriteProducts.count()
    pro=Product.objects.all().filter(is_active=True).order_by("id")
    if request.method =="GET":
        
        cs=request.GET.get("cs")
        
        
            
        if "searchName" in request.GET:
            name=request.GET.get("searchName")
            if name:
                if cs=="on":
                    pro=pro.filter(name__contains=name)
                    
                else:
                    pro=pro.filter(name__icontains=name)
                    
        if "searchDesc" in request.GET:
            description=request.GET.get("searchDesc")
            
            if description:
                if cs =="on":
                    pro=pro.filter(description__contains=description)
                else:
                    pro=pro.filter(description__icontains=description)
                
        if "priceFrom" in request.GET and "priceTo" in request.GET:
            priceFrom=request.GET.get("priceFrom")
            priceTo=request.GET.get("priceTo")
            if priceFrom and priceTo :
                if priceFrom.isdigit() and priceTo.isdigit():
                    pro=pro.filter(price__gte=priceFrom, price__lte=priceTo)
            

        
    context={
        'title':"products",
        "product":pro,
        'numCoffee':numCoffee,
        'countOrder':ContentCart,


    }
    return render(request, 'products/products.html',context)



# product

@login_required(login_url='signin')
def product(request,idProduct):
    user=userProfile.objects.get(userInfo=request.user)
    ContentCart=Order.objects.filter(user=request.user, is_delivered=False).count()
    numCoffee=user.favoriteProducts.count()
    pro= get_object_or_404(Product,id=idProduct)
    context={
        'title':"product",
        "product":pro,
        'numCoffee':numCoffee,
        'countOrder':ContentCart,

    }
    return render(request, 'products/product.html',context)

@login_required(login_url='signin')
def search(request):
    user=userProfile.objects.get(userInfo=request.user)
    ContentCart=Order.objects.filter(user=request.user, is_delivered=False).count()
    numCoffee=user.favoriteProducts.count()
    context={
        'title':"Search",
        'numCoffee':numCoffee,
        'countOrder':ContentCart,

    }
    return render(request, 'products/search.html',context)


        
    