from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.
# cookie--
def home(request):    
    # return render(request,'home.html')
    response = render(request, 'home.html')
    response.set_cookie('name','arif')
    response.set_cookie('name','karim', max_age=10) # second hisebe count hoy
    # response.set_cookie('name', 'karim', expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name':name})

def delete_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('name')
    return response

# Django Session:
def set_session(request):
    # data = {
    #     'name' : 'Rahim',
    #     'age' : 24,
    #     'language' : 'bangla'
    # }
    # print(request.session.get_session_cookie_age())
    # print(request.session.get_expiry_date())
    # request.session.update(data)
    request.session['name'] = 'karim'
    return render(request, 'home.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name', 'Guest')  
        request.session.modified = True   # after a 10 second it will be delete auto   
        # data = request.session
        return render(request,'get_session.html',{'name': name} )
    else:
        return HttpResponse("Your Session hasbeen expired. login again")

def delete_session(request):    
        # del request.session['name']
        request.session.flush()
        return render(request, 'del_session.html')
