
from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, './first_app/index.html', {"name": "I am Rahim",
    "marks" : 86, "list":[24,3,10,5], "blog": "amar sonar bangla ami tomay Valoa basi, chiro din tomar akash tomat batash amar prane oma amar prane bajay bashi sonar bangla ami tomay valobashi"})

    # return render(request, './first_app/index.html', {'courses': [
    #     {
    #         'id' : 1,
    #         'course' : 'C',
    #         'teacher' : 'Rahim'
    #     },
    #     {
    #         'id' : 2,
    #         'course' : 'C++',
    #         'teacher' : 'Karim'
    #     },
    #     {
    #         'id' : 3,
    #         'course' : 'Python',
    #         'teacher' : 'Sakib'
    #     }
    # ]})                                                  
 
