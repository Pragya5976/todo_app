from django.shortcuts import render , redirect
from todo_app.models import Task

def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST' :
        text = request.POST['task']
        task = Task.objects.create(text=text)
        task.save()
        return redirect('index')
    return render(request,'index.html',{'tasks':tasks})

def delete_task(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('index')
 
def edit_task(request,id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.text = request.POST['task']
        task.save()
        return redirect('index')
    return render(request,'edit.html',{'task':task})
  