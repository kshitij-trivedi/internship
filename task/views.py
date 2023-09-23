from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth import login as authlogin
from .forms import ImageForm
from .models import Image
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
         form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'upload.html', {'img':img, 'form':form})
    

def register(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        print(uname,email,pass1,pass2)
        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('/login')
    
        
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            authlogin(request,user)
            return redirect('/upload')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    
    return render(request,'login.html')


def logoutpage(request):
    logout(request)
    return redirect('/login')


