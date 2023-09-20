from typing import Any, Dict, List
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from book.forms import BookStoreForm 
from book.models import BookStoreModel
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse

# Create your views here.

# function based view:
# def home(request):
#     return render(request, 'home.html')


# class based view:
class MyTemplateView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)# argument ney
        context = {'name':'ABC', 'age':35}
        print(context)
        context.update(kwargs)# directory update kore
        print(context)
        return context


# function based view:
# def store_book(request):
#     if request.method == 'POST':        
#         book = BookStoreForm(request.POST)
#         if book.is_valid():
#            book.save(commit=True) 
#            print(book.cleaned_data)
#            return redirect('show_book')       
#     else:
#         book = BookStoreForm()
#     return render(request, 'store_book.html', {'form':book})



# 1. class based view:
# class BookFormView(FormView):
#     template_name = 'store_book.html'
#     form_class = BookStoreForm
#     # contex_object = 'booklist'
#     # success_url = '/show_book/'
#     success_url = reverse_lazy('show_book')
#     def form_valid(self,form):
#         print(form.cleaned_data)
#         form.save
#         # return HttpResponse('Form Submited')
#         return redirect('show_book')
    
# 2. class based view
class BookFormView(CreateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm    
    success_url = reverse_lazy('show_book')
    
    



# function based view:
# def show_book(request):
#     book = BookStoreModel.objects.all()
#     # print(book)
#     return render(request, 'show_book.html',{'data':book})


# class based view:
class bookListView(ListView):
    model= BookStoreModel
    template_name = 'show_book.html'
    context_object_name = 'booklist'
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter() # filter use for sorting
    # def get_context_data(self, **kwargs):
    #     context= super().get_context_data(**kwargs)
    #     context = {'tomal':BookStoreModel.objects.all().order_by('author')}
    #     return context
    # ordering = ["-id"]
    
    # Home work:
    # def get_template_names(self): #template k overide kore
    #     if self.request.user.is_superuser:
    #         template_name = ''
    #     elif self.request.user.is_stuff:
    #         template_name = ''
    #     else:
    #         template_name = self.template_name
    #     return [template_name]
    
    
class BookDetailsView(DetailView):
    model = BookStoreModel
    template_name = 'book_details.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'
    
    
        
# function based view:
def edit_book(request, id):
    book = BookStoreModel.objects.get(pk = id)
    form = BookStoreForm(instance = book)
    if request.method == 'POST':
        form = BookStoreForm(request.POST, instance = book )
        if form.is_valid():
           form.save()         
           return redirect('show_book')        
    return render(request, 'store_book.html', {'form':form})

# 1. class based view:
class BookUpDateview(UpdateView):
    form_class = BookStoreForm
    model = BookStoreModel
    template_name = 'store_book.html'
    success_url = reverse_lazy('show_book')
    


# function based view:
# def delete_book(request, id):
#     book = BookStoreModel.objects.get(pk = id).delete()          
#     return redirect('show_book')        
    
# class based view:
class DeleteBookView(DeleteView):
    model = BookStoreModel
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('show_book')    
    