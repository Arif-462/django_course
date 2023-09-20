from django.http import HttpResponse

def home(request):
    return HttpResponse ("<h1> This is my home page </h1>")