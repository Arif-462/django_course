from django.shortcuts import render
from .models import Product
from  category.models import Catgory
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

# Create your views here.

# product showing and pagination and category wise product display
def store(request, category_slug=None):       
    if category_slug:
        category= get_object_or_404(Catgory, slug = category_slug)
        products = Product.objects.filter(is_available = True, category = category)
        page = request.GET.get('page')
        print(page) 
        paginator = Paginator(products, 1) 
        paged_product = paginator.get_page(page)
        
    else:
        products = Product.objects.filter(is_available = True)
        page = request.GET.get('page')
        paginator = Paginator(products, 3)
        paged_product = paginator.get_page(page)
        for i in paged_product:
            print(i)
        print(paged_product.has_next, paged_product.has_previous, paged_product.previous_page_number, paged_product.next_page_number)
    
    categories = Catgory.objects.all()
    # for item in products:
    #     print(item.product_name, item.price, item.is_available)
    context = {'products':paged_product, 'categories':categories}
    return render(request, 'store/store.html', context )



def product_details(request, category_slug, product_slug):
    single_product = Product.objects.get(slug = product_slug, category__slug = category_slug)
    return render(request, 'store/product_detail.html',{'product': single_product})