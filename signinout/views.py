from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    user_data = User.objects.all()

    return render(request,'index.html',{'user_data':user_data})

def project(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'project.html')

def chats(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'chats.html')

def profile(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'profile.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('psw')
        pass2 = request.POST.get('cpsw')

        new_user = User.objects.create_user(username,email,pass1)
        new_user.save()
        return redirect('/login')
    return render(request,'signup.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')
    
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')
