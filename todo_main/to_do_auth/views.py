from django.shortcuts import render,HttpResponse, redirect
# from to_do_auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from to_do_app.views import index
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login


# Create your views here.
def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.objects.get(username=form.username)
             
             
            login(request, user)
    return render (request,'auth/login.html',{'form':form})

def singup(request):
    print('this si singup page')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        print('post request has been made')
        if form.is_valid():
            
            print('form is valid')
            user = form.save()
            login(request, user)
            return redirect('to_do:index')
    else:
        print('thsi si else condition')
        form = UserCreationForm()

        
    
        
    return render(request, 'auth/singup.html',{'form':form,'title':'tile'})