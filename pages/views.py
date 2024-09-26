from django.shortcuts import render,redirect
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import userProfile
from order.models import Order

# Create your views here.
@login_required(login_url='signin')
def index(request):
    user=userProfile.objects.get(userInfo=request.user)
    ContentCart=Order.objects.filter(user=request.user, is_delivered=False).count()
    
    numCoffee=user.favoriteProducts.all().count()
    pro=Product.objects.all().filter(is_active=True).order_by("-id")[:8]
    context={
        "title":'home',
        "latesproduct":pro,
        'numCoffee':numCoffee,
        'countOrder':ContentCart,

    }
    return render(request, 'pages/index.html',context)

@login_required(login_url='signin')
def about(request):
    user=userProfile.objects.get(userInfo=request.user)
    ContentCart=Order.objects.filter(user=request.user, is_delivered=False).count()
    
    numCoffee=user.favoriteProducts.all().count()
    context={
        "title":'about',
        'numCoffee':numCoffee,
        'countOrder':ContentCart,

    }
    return render(request, 'pages/about.html',context)


@login_required(login_url='signin')
def coffee(request):
    user=userProfile.objects.get(userInfo=request.user)
    ContentCart=Order.objects.filter(user=request.user, is_delivered=False).count()
    
    numCoffee=user.favoriteProducts.all().count()
    context={
        "title":'coffee',
        'numCoffee':numCoffee,
        'countOrder':ContentCart,

    }
    return render(request, 'pages/coffee.html',context)

@login_required(login_url='signin')
def favorite(request):
    # number of coffee
    user=userProfile.objects.get(userInfo=request.user)
    ContentCart=Order.objects.filter(user=request.user, is_delivered=False).count()
    
    numCoffee=user.favoriteProducts.all().count()
    favoriteCoffee=user.favoriteProducts.all()
    
    context={
        'title':'favoriteCoffee',
        'numCoffee':numCoffee,
        'favoriteCoffee':favoriteCoffee,
        'countOrder':ContentCart,

    }
    
    return render(request, 'pages/favorite.html', context)

@login_required(login_url='signin')
def delfavorite(request,proID):
    # number of coffee
    user=userProfile.objects.get(userInfo=request.user)
    
    deletefavarite=user.favoriteProducts.get(id=proID)
    if deletefavarite:
        user.favoriteProducts.remove(deletefavarite)
    return redirect('favorite')
    
    
