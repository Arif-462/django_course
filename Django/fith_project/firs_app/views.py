from django.shortcuts import render
from . forms import contactForm, studentData,passwordValidation

# Create your views here.
def home(request):
    return render(request, "./first_app/home.html")

def about(request):
    # return render(request, "./first_app/about.html")
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, './first_app/about.html', {'name': name, 'email': email,
                'select':select})
    else:   
        return render(request, "./first_app/about.html")

        

def submit_form(request):
    # print(request.POST)
    # if request.method == 'POST':
    #     name = request.POST.get('username')
    #     email = request.POST.get('email')
    #     return render(request, './first_app/form.html', {'name': name, 'email': email})
    # else:
    return render(request, './first_app/form.html')

def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST,request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./firs_app/upload/'+ file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)         
    else:
        form = contactForm()
    return render(request, './first_app/django_form.html', {'form': form })
    


def StudentForm(request):
    if request.method == 'POST':
        form = studentData(request.POST,request.FILES)
        if form.is_valid():            
            print(form.cleaned_data)         
    else:
        form = studentData()
    return render(request, './first_app/django_form.html', {'form': form })
    

def check_valid_password(request):
    if request.method == 'POST':
        form = passwordValidation(request.POST)
        if form.is_valid():            
            print(form.cleaned_data)         
    else:
        form = passwordValidation()
    return render(request, './first_app/django_form.html', {'form': form })
    