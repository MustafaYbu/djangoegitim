from django.shortcuts import render,redirect
from . forms import Loginform,Registerform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from courses.models import Course
from django.contrib.auth.models import  User


# Create your views here.
def user_login(request):
    if request.method=='POST':
        form=Loginform(request.POST)
        if form.is_valid():
            #kadi ve sifre alinacak sayfadan//
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            #kullanici var mi yokmu o sorulup olusturulacak
            user=authenticate(request,username=username,password=password)
            if user is not None:
                if user.is_active:
                 login(request,user)
                 return  redirect('index')
                else:
                    messages.info(request,'DISABLED ACCOUNT')
            else:
                messages.info(request,'USERNAME OR PASSWORD IN CORRECT')
    else:
        form=Loginform()

    
    return render(request,'login.html',{'form':form})


 

def user_logout(request):
    logout(request)
    return redirect('index')

def user_register(request): 

    if request.method=='POST':
        form=Registerform(request.POST)
        if form.is_valid():
          form.save()            
          messages.success(request,'account has been created,Please Login')
          return  redirect('userlogin')
        
    else :
        form=Registerform()
    
       
    return render(request,'register.html',{'form':form})

@login_required(login_url='userlogin')
def user_dashboard(request):
    girisyapankullanici=request.user
    courses = girisyapankullanici.courses_joined.all()

    context = {
        'kurs': courses
    }

    return render(request, 'dashboard.html', context)

def kursakayitol(request):
    course_id = request.POST['course_id']
    user_id = request.POST['user_id']
    course = Course.objects.get(id = course_id)
    user = User.objects.get(id = user_id)
    course.musteriler.add(user)
    return redirect('userdashboard')
