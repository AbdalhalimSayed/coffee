from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Order
from products.models import Product
from accounts.models import userProfile

# Create your views here.
@login_required(login_url='signin')
def orders(request):
    if request.method == "POST" and 'btnCart' in request.POST:
        qyt = request.POST.get('qyt')  # Corrected variable name 'qyt' instead of 'gyt'
        proID = request.POST.get('id')
        try:
            pro = Product.objects.get(id=proID)
            try:
                order = Order.objects.get(user=request.user, product=pro,is_delivered=False)
                order.quantity = qyt
                order.totalPrice = pro.price * int(qyt)
                order.save()
                messages.success(request, "Updated product in your cart successfully.")
            except Order.DoesNotExist:
                new_order = Order(user=request.user, product=pro, totalPrice=pro.price * int(qyt), quantity=qyt)
                new_order.save()
                messages.success(request, "Added product to your cart successfully.")
        except Product.DoesNotExist:
            messages.error(request, "The product does not exist.")
    
    return redirect('product', idProduct=proID)
            

@login_required(login_url='signin')
def Carts(request):
    TotalPrice=0
    user=userProfile.objects.get(userInfo=request.user)

    ContentCart=Order.objects.filter(user=request.user, is_delivered=False).order_by("product")
    numCoffee=user.favoriteProducts.all().count()

    allOrder=ContentCart.count()
    for p in ContentCart:
        TotalPrice+=p.totalPrice
        
    context={
        'ContentCart':ContentCart,
        'priceOrders':TotalPrice,
        'countOrder':allOrder,
        'numCoffee':numCoffee,
        'title':'cart',
    }
    return render(request, 'pages/cart.html', context)


@login_required(login_url='signin')
def deleteOrder(request,cartID):
    delorder=Order.objects.filter(id=cartID,user=request.user)
    delorder.delete()
    messages.success(request, 'Success Delete Order.')
    return redirect('cart')
    
    
@login_required(login_url='signin')
def sumQuantity(request,orderID):
    if request.user.is_authenticated:
        order=Order.objects.get(id=orderID, is_delivered=False, user=request.user)
        order.quantity +=1
        order.totalPrice = order.product.price * order.quantity
        order.save()
    else:
         return redirect('signin')
    return redirect('cart')

@login_required(login_url='signin')
def subQuantity(request, orderID):
    if request.user.is_authenticated:
        order=Order.objects.get(id=orderID, is_delivered=False, user=request.user)
        if order.quantity == 1:
            pass
        else:
            order.quantity -=1
            order.totalPrice = order.product.price * order.quantity
            order.save()
    else:
         return redirect('signin')
    return redirect('cart')