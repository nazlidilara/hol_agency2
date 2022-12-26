from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginUserForm,NewUserForm,User
from django.contrib.auth.forms import PasswordChangeForm,PasswordResetForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UserForm,ProfileForm
import uuid


# Giriş  fonksiyonu
def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = LoginUserForm(request,data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                return render(request,'login.html',{'form': form})
        else:
            return render(request,'login.html',{'form': form})

    else:
        form = LoginUserForm()
        return render(request,'login.html',{'form': form})


# Kayıt ol  fonksiyonu
def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            last_name = form.cleaned_data.get("last_name")
            user = authenticate(request,username=username,password=password,last_name=last_name)
            login(request,user,)
            return redirect("home")
        else:
            return render(request,"register.html",{"form": form})
    else:
        form = NewUserForm()
        return render(request,"register.html",{"form": form})






# Çıkış fonskiyonu
def logout_request(request):
    logout(request)
    return redirect("login_request")



