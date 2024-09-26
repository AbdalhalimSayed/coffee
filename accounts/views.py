from django.shortcuts import render,redirect,get_object_or_404
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout ,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import userProfile
from products.models import Product
from django.contrib.auth.decorators import login_required
from order.models import Order
# Create your views here.

def signIn(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method== "POST" and "btnSignIn" in request.POST:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request, username=username, password=password)
            if user is not None:
                if 'rm' not in request.POST:
                    request.session.set_expiry(0)
                login(request,user)
                return redirect('index')
            else:
                messages.error(request, "the password or username is notvalid")

        context={
            'title':"Sign In",
        }
        return render(request, 'accounts/signin.html',context)
    
    # register
    
def register(request):
    context={
        'title':"register",
    }
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST' and "btnRegister" in request.POST:
            fname=None
            lname=None
            address1=None
            address2= None
            city=None
            state =None
            zipcode=None
            email=None
            password=None
            username=None
            agree=None
            if 'fname' in request.POST: fname=request.POST.get('fname')
            else:messages.info(request, "this not correct fname")
            
            if 'lname' in request.POST: lname=request.POST.get('lname')
            else: messages.info(request, "this not correct lname")
            
            if 'address1' in request.POST: address1=request.POST.get('address1')
            else: messages.info(request, "this not correct address1")
            
            if 'address2' in request.POST: address2=request.POST.get('address2')
            else: messages.info(request, "this not correct address2")
            
            if 'city' in request.POST: city=request.POST.get('city')
            else:messages.info(request, "this not correct city")
                
            if 'state' in request.POST:state=request.POST.get('state')
            else:messages.info(request, "this not correct state")
            
            if 'zipcode' in request.POST: zipcode=request.POST.get('zipcode')
            else:messages.info(request, "this not correct zipcode")
            
            if 'email' in request.POST: email=request.POST.get('email')
            else:messages.info(request, "this not correct email")
            
            if 'username' in request.POST: username=request.POST.get('username')
            else:messages.info(request, "this not correct username")
            
            if 'password' in request.POST: password=request.POST.get('password')
            else:messages.info(request, "this not correct password")
            
            if "agree" in request.POST: agree= request.POST.get('agree')
            # check value
            if fname and lname and address1 and address2 and city and state and zipcode and email and username and password:
                    
                if agree == "on":
                    # check username
                    if User.objects.all().filter(username=username).exists():
                        messages.error(request, "username is exists")
                    else:
                        if User.objects.all().filter(email=email).exists():
                            messages.error(request, "use other email")
                        else:
                            try:
                                validate_email(email)
                                addData=User.objects.create_user(
                                    first_name=fname,
                                    last_name=lname,
                                    username=username,
                                    email=email,
                                    password=password
                                    )
                                addData.save()
                                # add other user profile 
                                userInfor=userProfile(
                                    userInfo=addData,
                                    address=address1,
                                    address2=address2,
                                    city=city,
                                    state=state,
                                    zipCode=zipcode
                                )
                                userInfor.save()
                                
                                
                                return redirect("signin")
                            except ValidationError:
                                messages.error(request,'invalid email')                           
                else:
                    messages.error(request, "Please agree the policy")
                    
            else:
                messages.error(request, "some fields is empty ")
            context={
                'title':"register",
                'fname':fname,
                'lname':lname,
                'address1':address1,
                'address2':address2,
                'city':city,
                'state':state,
                'zipcode':zipcode,
                'email':email,
                'username':username,
                'password':password,
            }
            return render(request, 'accounts/register.html',context)
                
        else:
            return render(request, 'accounts/register.html',context)

    
    

# Edit profile
@login_required(login_url='signin')
def profile(request):
    user=User.objects.get(username=request.user)
    ContentCart=Order.objects.filter(user=request.user, is_delivered=False).count()
    
    userInformation=userProfile.objects.get(userInfo=request.user)
    if request.method == "POST" and "btnSave" in request.POST:
        if request.POST.get("fname") and request.POST.get("lname") and request.POST.get("address1") and request.POST.get("address2") and request.POST.get("city") and request.POST.get("state") and request.POST.get("zipcode") and request.POST.get("password"):
            user.first_name = request.POST.get("fname")
            user.last_name = request.POST.get("lname")
            user.set_password(request.POST.get("password"))
            userInformation.address=request.POST.get("address1")
            userInformation.address2=request.POST.get("address2")
            userInformation.city=request.POST.get("city")
            userInformation.zipCode=request.POST.get("zipcode")
            userInformation.state=request.POST.get("state")
            userInformation.save()
            
            user.save()
            messages.success(request, "Your Profile Is Update Successfully.")
        else:
            messages.error(request, "Exists Fileds Is Empty.")
    user=User.objects.get(username=request.user)
    userInformation=userProfile.objects.get(userInfo=request.user)
    numCoffee=userInformation.favoriteProducts.all().count()
    context={
        'title':"edit profile",
        "userProfile":user,
        "userInformation":userInformation,
        'numCoffee':numCoffee,
        'countOrder':ContentCart,

    }
    return render(request, 'accounts/profile.html',context)

@login_required(login_url='signin')
def LogOut(request):
    logout(request)
    return redirect('signin')


# favorite product
@login_required(login_url="signin")
def addFovarite(request,proID):

    if request.user.is_authenticated:
        try:
            if userProfile.objects.get(userInfo = request.user):
                try:
                    if userProfile.objects.get(favoriteProducts=proID, userInfo = request.user):
                        messages.warning(request, 'The Coffee Is Exists.')
                        return redirect('product',idProduct=proID)
                except userProfile.DoesNotExist:
                    pro=Product.objects.get(id=proID)
                    user=userProfile.objects.get(userInfo=request.user)
                    user.favoriteProducts.add(pro)
                    user.save()
                    messages.success(request,'Successfully Add Coffee To Your Fovarite.')
                    return redirect('product',idProduct=proID)
            
        except userProfile.DoesNotExist:
            return redirect('product',idProduct=proID)
    
    
