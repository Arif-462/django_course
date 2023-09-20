from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse ("<h1>This is my first django page</h1>")
def about(request):
    return HttpResponse ("<h1>This is my about page</h1>")
def contact(request):
    return HttpResponse ("<h1>This is my contact page</h1>")