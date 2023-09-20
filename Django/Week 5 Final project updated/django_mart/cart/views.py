from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from cart.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
#https://github.com/abdullahallnaim/django_mart/blob/master/cart/views.py


def get_cart_id(request): # session created as cart id from this function
    cart= request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id) # get th product
    current_user = request.user  
    
    if current_user.is_authenticated:
        # print('authenticated')
        cart_item_exists= CartItem.objects.filter(product=product, user = current_user).exists()
        if cart_item_exists:
            cart_items = CartItem.objects.filter(product = product, user= current_user)
            item = CartItem.objects.get(product = product, user= current_user)
            item.quantity += 1
            item.save()           
        
        else:
            try:
                cart = Cart.objects.get(cart_id = get_cart_id(request))
            except Cart.DoesNotExist:
                cart = Cart.objects.create(
                    cart_id = get_cart_id(request)
                )
            cart.save()
            # cartId = Cart.objects.get(cart_id = session_id)
            cart_item = CartItem.objects.create(
                cart = cart,
                product = product,
                quantity = 1,
                user = current_user
            )
            cart_item.save()
        return redirect('cart')
        
    else:   
        product = Product.objects.get(id=product_id)
        try:
            cart = Cart.objects.get(cart_id = get_cart_id(request)) # get cart
        except Cart.DoesNotExist:
            cart = Cart.objects.create(
                cart_id = get_cart_id(request)
            )
            cart.save()
        
        try:
            cart_item = CartItem.objects.get(product=product, cart = cart)
            cart_item.quantity += 1
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart,
            )
            cart.save()
    return redirect('cart')
            



def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=get_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass #just ignore

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax'       : tax,
        'grand_total': grand_total,
    }
    return render(request, 'cart/cart.html', context)



def remove_cart_item(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=request.user)
        else:
            cart = Cart.objects.get(cart_id=get_cart_id(request))
            cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')


    
    # product = Product.objects.get(id=product_id)
    # session_id = get_create_session(request)
    # cartId = Cart.objects.get(cart_id = session_id) # cart search korlam
    # cart_item = CartItem.objects.get(cart=cartId, product=product)# cart item filter korlam product and cart er vittite
    # print(cart_item)
    # if cart_item.quantity > 1:
    #     cart_item.quantity -= 1
    #     cart_item.save()
    # else:
    #     cart_item.delete()
    # return redirect('cart')
    
   

def remove_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=request.user)
        else:
            cart = Cart.objects.get(cart_id=get_cart_id(request))
            cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')



# def remove_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     session_id = request.session.session_key
#     cartId = Cart.objects.get(cart_id = session_id)# cart search korlam
#     cart_item = CartItem.objects.get(cart=cartId, product=product)# cart item filter korlam product and cart er vittite
#     cart_item.delete()
#     return redirect('cart')  











# def _cart_id(request):# session created from this function
#     cart = request.session.session_key
#     if not cart:
#         request.session.create()
#     return cart


# def add_to_cart(request, product_id):
#     current_user = request.user
#     product = Product.objects.get(id=product_id) #get the product
#     # If the user is authenticated
#     if current_user.is_authenticated:
#         is_cart_item_exists = CartItem.objects.filter(product=product, user=current_user).exists()
#         if is_cart_item_exists:
#             cart_items = CartItem.objects.filter(product=product, user=current_user)
#             print(cart_items)
#             item = CartItem.objects.get(product=product, user=current_user)
#             item.quantity += 1
#             item.save()
            
#         else:
#             try:
#                 cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using the cart_id present in the session
#             except Cart.DoesNotExist:
#                 cart = Cart.objects.create(
#                     cart_id = _cart_id(request)
#                 )
#             cart.save()
#             cart_item = CartItem.objects.create(
#                 product = product,
#                 quantity = 1,
#                 cart = cart,
#                 user = current_user
#             )
#             cart_item.save()
#         return redirect('cart')
#     else:
#         product = Product.objects.get(id=product_id)
#         try:
#             cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart using the cart_id present in the session
#         except Cart.DoesNotExist:
#             cart = Cart.objects.create(
#                 cart_id = _cart_id(request)
#             )
#             cart.save()
        
#         try:
#             cart_item = CartItem.objects.get(product=product, cart=cart)
#             cart_item.quantity  += 1
#             cart_item.save()
#         except CartItem.DoesNotExist:
#             cart_item = CartItem.objects.create(
#                     product = product,
#                     quantity = 1,
#                     cart = cart,
#                 )
#             cart.save()
#     return redirect('cart')



# def remove_cart(request, product_id, cart_item_id):

#     product = get_object_or_404(Product, id=product_id)
#     try:
#         if request.user.is_authenticated:
#             cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
#         else:
#             cart = Cart.objects.get(cart_id=_cart_id(request))
#             cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
#         if cart_item.quantity > 1:
#             cart_item.quantity -= 1
#             cart_item.save()
#         else:
#             cart_item.delete()
#     except:
#         pass
#     return redirect('cart')


# def remove_cart_item(request, product_id, cart_item_id):
#     product = get_object_or_404(Product, id=product_id)
#     if request.user.is_authenticated:
#         cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
#     else:
#         cart = Cart.objects.get(cart_id=_cart_id(request))
#         cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
#     cart_item.delete()
#     return redirect('cart')


# def cart(request, total=0, quantity=0, cart_items=None):
#     try:
#         tax = 0
#         grand_total = 0
#         if request.user.is_authenticated:
#             cart_items = CartItem.objects.filter(user=request.user, is_active=True)
#         else:
#             cart = Cart.objects.get(cart_id=_cart_id(request))
#             cart_items = CartItem.objects.filter(cart=cart, is_active=True)
#         for cart_item in cart_items:
#             total += (cart_item.product.price * cart_item.quantity)
#             quantity += cart_item.quantity
#         tax = (2 * total)/100
#         grand_total = total + tax
#     except ObjectDoesNotExist:
#         pass #just ignore

#     context = {
#         'total': total,
#         'quantity': quantity,
#         'cart_items': cart_items,
#         'tax'       : tax,
#         'grand_total': grand_total,
#     }
#     return render(request, 'cart/cart.html', context)






















# def get_create_session(request):# session created from this function
#     if not request.session.session_key:
#         request.session.create()
#     return request.session.session_key



# def cart(request):
#     cart_items = None
#     tax = 0
#     total = 0
#     grand_total = 0
#     if request.user.is_authenticated:
#         cart_items = CartItem.objects.filter(user = request.user)
#         print(cart_items)
#         for item in cart_items:
#             total += item.product.price * item.quantity
        
#     else:
#         session_id = get_create_session(request)
#         # print(session_id)
#         carID = Cart.objects.get(cart_id = session_id)
#         cart_id = Cart.objects.filter(cart_id = session_id).exists()
#         cart_items = None
    
#         if cart_id:
#             cart_items = CartItem.objects.filter(cart = carID)
#             print(cart_items)
#             for item in cart_items:
#                 total += item.product.price * item.quantity
#     tax = (2*total)/100
#     grand_total = total + tax       
#     return render(request, 'cart/cart.html', {'cart_items':cart_items, 'total':total, 'tax': tax, 'grand_total': grand_total})







# def add_to_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     session_id = get_create_session(request)    
    
#     if request.user.is_authenticated:
#         # print('authenticated')
#         cart_item = CartItem.objects.filter(product=product, user = request.user).exists()
#         if cart_item:
#             item = CartItem.objects.get(product = product, user= request.user)
#             item.quantity += 1
#             item.save()           
        
#         else:
#             # cartId = Cart.objects.get(cart_id = session_id)
#             item = CartItem.objects.create(
#                 # cart = cartId,
#                 product = product,
#                 quantity = 1,
#                 user = request.user
#             )
#             item.save()
        
#     else:      
#         cart_id = Cart.objects.filter(cart_id = session_id).exists()    
#         if cart_id:
#             cart_item = CartItem.objects.filter(product=product).exists()
#             if cart_item:
#                 item = CartItem.objects.get(product = product)
#                 item.quantity += 1
#                 item.save()           
            
#             else:
#                 cartId = Cart.objects.get(cart_id = session_id)
#                 item = CartItem.objects.create(
#                     cart = cartId,
#                     product = product,
#                     quantity = 1
#                 )
#                 item.save()    
#         else:
#             cart = Cart.objects.create(
#             cart_id = session_id
#             )    
#             cart.save()   
#     return redirect('cart')



# def remove_cart_item(request, product_id):
#     # print(product_id)
#     product = Product.objects.get(id=product_id)
#     session_id = get_create_session(request)
#     cartId = Cart.objects.get(cart_id = session_id) # cart search korlam
#     cart_item = CartItem.objects.get(cart=cartId, product=product)# cart item filter korlam product and cart er vittite
#     print(cart_item)
#     if cart_item.quantity > 1:
#         cart_item.quantity -= 1
#         cart_item.save()
#     else:
#         cart_item.delete()
#     return redirect('cart')
    
   


# def remove_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     session_id = request.session.session_key
#     cartId = Cart.objects.get(cart_id = session_id)# cart search korlam
#     cart_item = CartItem.objects.get(cart=cartId, product=product)# cart item filter korlam product and cart er vittite
#     cart_item.delete()
#     return redirect('cart')  







