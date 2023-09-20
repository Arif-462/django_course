from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, './first/index.html', {"name" : "I am Rahim", "marks" : 86, 
    "courses" : [
              {
            'id' : 1,
            'course' : 'C',
            'teacher' : 'Rahim'
        },
        {
            'id' : 2,
            'course' : 'C++',
            'teacher' : 'Karim'
        },
        {
            'id' : 3,
            'course' : 'Python',
            'teacher' : 'Sakib'
        }
    ]})
    
def about(request):
    # return HttpResponse(' I am in http ')
    return render(request, './first/about.html', {'author' : 'rakib babu'})