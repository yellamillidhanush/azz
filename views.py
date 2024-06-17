from django.shortcuts import render
from django.contrib.auth import authenticate,login
from amazon.models import createaccount
from django.contrib.auth.models import User
from . import models

# Create your views here.
def loginform(request):
    if request.method=='POST':
        email=request.POST['uname']
        password=request.POST['pwd']
        validateuser=authenticate(request,username=email,password=password)
        if validateuser!=None:
            login(request,validateuser)
            return render(request,'amazon/home.html')
        else:
            return render(request,'amazon/login.html',{'msg':'incorrect details'})

    return render(request,'amazon/login.html')



def createaccount(request):
    if request.method=='POST':
        name=request.POST['t1']
        email=request.POST['t2']
        password=request.POST['t3']
        if User.objects.filter(email__iexact=email).exists():
            return render(request,'amazon/createaccount.html',{'msg':'This email is already registered'})
        else:
            my_user=User.objects.create_user(username=name,email=email,password=password)
            my_user.save()
            return render(request,'amazon/createaccount.html',{'msg':'Account created sucessfully'})
    return render(request,'amazon/createaccount.html')
        
















'''if models.createaccount.objects.filter(email__iexact=email).exists():
            return render(request,'amazon/createaccount.html',{'msg':'This email is already registered'})
       
        else:
            models.createaccount.objects.create(name=name,email=email,password=password)
            return render(request,'amazon/createaccount.html',{'msg':'Account created sucessfully'})
    return render(request,'amazon/createaccount.html')'''





def forgotpassword(request):
    return render(request,'amazon/forgotpass.html')




def terms(request):
    return render(request,'amazon/terms.html')