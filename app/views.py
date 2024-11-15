from django.shortcuts import render, redirect
from django.views import View

# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from .models import User
from django.utils.timezone import timedelta,now
import datetime


class index(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, "index.html")


class loginview(View):
    def get(self, request):
        return render(request, "Login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
            if user != None:
                login(request, user)
                return redirect("index/")
            else:
                print("invalid Crendentials")
                messages.error(request, f"Invalid Credentials")
        else:
            messages.error(request, f"Username not found")

        return render(request, "Login.html")


class signup(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        phoneNo = request.POST.get("phoneNo")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(email=email).exists():
            print("email is taken")
            messages.error(request, f"email is already taken")

        elif User.objects.filter(username=username).exists():
            print("username is taken")
            messages.error(request, f"user is already taken")

        else:
            User.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                phoneNo=phoneNo,
                email=email,
                username=username,
                password=password,
            )
            print("registration successfull please login ")
            messages.success(request, f"Registration successfull ! Please login ")
            return redirect("/")

        return render(request, "signup.html")


class logoutview(View):
    def get(self, request):
        logout(request)
        return redirect("/")

class Forgot(View):
    def get(Self, request):
        return render(request, "forgot.html")
    
    def post(self, request):
        email = request.POST.get("email")
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email = email)
            exp_date = datetime.datetime.now()+ datetime.timedelta(hours = 2)
            


class Resetpassword(View):
    def get(self, request):
        return render(request, "resetpassword.html")