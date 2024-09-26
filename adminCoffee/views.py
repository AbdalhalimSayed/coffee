from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from products.models import Product
from order.models import Order
from accounts.models import userProfile
# Create your views here.
@login_required(login_url='signin')
def dashboard(request):
    users=User.objects.all().filter(is_superuser=False,is_active=True,is_staff=False).reverse()[:11]
    orders=Order.objects.all().filter(is_delivered=False)
    products=Product.objects.all().filter(is_active=True)
    context={
        'customer':users.count(),
        'orders':orders.count(),
        'products':products.count(),
        'dataCustomer':users,
    }
    return render(request, 'adminCoffee/dashboard.html',context)

@login_required(login_url="signin")
def customer(request):
    alldata = userProfile.objects.filter(
        userInfo__is_active=True,
        userInfo__is_superuser=False,
        userInfo__is_staff=False
    )
    context={
        'customers':alldata,
    }
    return render(request, 'adminCoffee/customer.html',context)

@login_required(login_url="signin")
def order(request):
    return render(request, 'adminCoffee/order.html')

@login_required(login_url="signin")
def addcoffee(request):
    return render(request, 'adminCoffee/addcoffee.html')

@login_required(login_url="signin")
def customeraction(request,userid):
    user=get_object_or_404(
        User,
        id=userid,
        is_active=True,
        is_superuser=False,
        is_staff=False
    )
    alldata=userProfile.objects.get(userInfo=user)
    
    context={
        'customer':alldata,
    }
    return render(request, 'adminCoffee/customeraction.html',context)

