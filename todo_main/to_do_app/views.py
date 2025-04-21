from django.http import HttpResponse
from django.shortcuts import render ,get_object_or_404, redirect
from to_do_app.models import todo
from django.contrib.auth.decorators import login_required




def index(request):
    if request.user.is_authenticated:
        
        todos = todo.objects.all()
        for i, task in enumerate(todos, start=1):
            task.display_number = i
        return render(request, 'to_do_app/index.html', {'todos': todos})
    
    return redirect('to_do_auth:singup')
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        new_task = todo(title=title)
        new_task.save()
    return redirect('to_do:index')

def delete (request,id):
    todo.objects.get(id=id).delete()
    return redirect('to_do:index')

def update (request,id):
    to_do_object = get_object_or_404(todo, pk = id)
    if request.method == 'POST':
        if request.POST.get('isCompleted') == 'on':
            iscompleted =  request.POST.get('isCompleted')
            print(iscompleted)
            if iscompleted :    
                print('inside funtion iscomplete')
                to_do_object.isCompleted = True
        else:
             to_do_object.isCompleted = False
        to_do_object.title = request.POST.get('title')

        to_do_object.save()
            
    return redirect('to_do:index')