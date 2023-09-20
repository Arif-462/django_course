from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login,logout, authenticate
from cart.models import Cart, CartItem



# Create your views here.

def get_create_session(request):# session created from this function
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def get_cart_id(request): # session created as cart id from this function
    cart= request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form  = RegistrationForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data.get('username'))
            user = form.save()
            login(request, user)
            return redirect('cart')
    return render(request,'accounts/register.html',{'form':form})

def profile(request):
    return render(request, 'accounts/dashboard.html')

def user_login(request):
    if request.method == 'POST':
        # print(request.POST)
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)
        # print(user)
        session_key = get_cart_id(request)
        cart = CartItem.objects.get(cart_id = session_key)
        is_cart_item_exists =CartItem.objects.filter(cart=cart, user = user ).exists()
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(cart= cart)
            for item in cart_item:
                item.user = user
                item.save()            
            login(request, user)        
        return redirect('profile')
    return render(request, 'accounts/signin.html')

def user_logout(request):
    logout(request)
    return redirect('login')
