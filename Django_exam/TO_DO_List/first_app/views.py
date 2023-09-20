from django.shortcuts import render,redirect
from first_app.forms import Task_Form
from first_app.models import Task_Model
# from django.views.generic.edit import FormView, CreateView, UpdateView,DeleteView
# from django.urls import reverse_lazy


# Create your views here.

def home(request):
    return render(request, 'base.html')

def show_task(request):
    task = Task_Model.objects.all()   
    return render(request, 'show_task.html',{'task':task})

def add_task(request):
    if request.method == 'POST':        
        form = Task_Form(request.POST)
        if form.is_valid():
           form.save(commit=True)            
           return redirect('show_task')       
    else:
        form = Task_Form()
    return render(request, 'add_task.html', {'form':form})

def edit_task(request, id):
    task = Task_Model.objects.get(pk = id)
    form = Task_Form(instance = task)
    if request.method == 'POST':
        form = Task_Form(request.POST, instance = task )
        
        if form.is_valid():
           form.save() 
           task.is_completed = False        
           return redirect('show_task')        
    return render(request, 'add_task.html', {'form':form})

def delete_task(request, id):
    task = Task_Model.objects.get(pk = id).delete()          
    return redirect('show_task')


def completed_task(request, id):
    task = Task_Model.objects.get(pk = id)
    task.is_completed = True       
    task.save()  
    return render(request, 'completed.html', {'task':task})
    
        
def completed_task_list(request):
    task = Task_Model.objects.filter(is_completed=True)  
    print(task)    
    return render(request, 'completed.html', {'task':task})
    
     



  

