from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from .models import *
# Create your views here.
def indexpage(request):
 return render(request,'index.html')

def login(request):
  if request.method=="POST":
        uname=request.POST['username']
        passw=request.POST['password']
        print(uname,passw)
        user=auth.authenticate(username=uname,password=passw)
        print(user)
        if user is not None:
            print("yes")
            auth.login(request,user)
            if request.user.is_authenticated:
                print("yes ")
                return HttpResponseRedirect('/')
        else:
            
            print("no")
            # messages.info(request,"password or username is incorrect or createaccount first")
            return render(request,'signup.html')
  return render(request,'login.html')
def signup(request):
  if request.method=="POST":
    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    password=request.POST['password']
    print(username,password)
    if User.objects.filter(username=username).exists():
                print("hai bhai")
                return render(request,'login.html')
                
                
    else:
                print("nhi hai ")    
                user=Userdetails.objects.create_user(username=username,first_name=firstname,password=password,email=email,last_name=lastname)
                user.save()
                return redirect('/')

  return render(request,"signup.html")

def logout(request):
     auth.logout(request)
     return redirect('/')