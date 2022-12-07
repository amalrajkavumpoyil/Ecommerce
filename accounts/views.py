from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("user created")
        else:
            print("password does not match")
            return redirect('register')

        return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    if request.method == "POST":
        print("----------------------------------------------------------------------")
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user:
            print("------------------------------------------------------------")
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'please check your details')
            return redirect('login')
    else:
        return render(request, "login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
