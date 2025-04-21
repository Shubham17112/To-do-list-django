from django.shortcuts import render,HttpResponse, redirect
# from to_do_auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from to_do_app.views import index
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def login(request):
    return HttpResponse ("login page")

def singup(request):
    print('this si singup page')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        print('post request has been made')
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('to_do:index')
    else:
        print('thsi si else condition')
        form = UserCreationForm()

        
    
        
    return render(request, 'auth/singup.html',{'form':form,'title':'tile'})