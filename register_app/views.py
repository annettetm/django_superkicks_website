from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpass=request.POST.get('confirmpass')
        if password==confirmpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('http://127.0.0.1:8000/register/')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect('http://127.0.0.1:8000/register/')
            else:
                user= User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                user.save()
                messages.info(request,'User is created')
                return redirect('/')
        else:
            messages.info(request,"Password is not matching")
            return redirect('http://127.0.0.1:8000/register/')
    else:
    
        return render(request,"register.html")

def login(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Enter valid username and password")
            return redirect('http://127.0.0.1:8000/register/')
    else:
        return render(request,"signin.html")
        
def signout(request):
    auth.logout(request)
    return redirect('/') 


    

