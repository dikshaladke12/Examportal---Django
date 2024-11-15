from django.shortcuts import render, redirect
from django.views import View

# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from .models import *

from pytz import timezone
import datetime
import random
import uuid
from django.conf import settings
from django.core.mail import send_mail
import pytz

utc=pytz.UTC

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
            userdata= User.objects.get(username=username)
           
            if user != None:
                login(request, user)
                if userdata.is_superuser:
                    return redirect('index/')
                return redirect("questions/")
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
            user = User.objects.get(email=email)
            exp_date = datetime.datetime.now() + datetime.timedelta(hours=2)
            uuid_data = uuid.uuid1(random.randint(0, 281474976710655))
            forgot = resetuuid.objects.create(
                UUID=uuid_data, user=user, expiry=exp_date
            )

            url = f"{settings.SITE_URL}/reset/{forgot.UUID}"
            if email:
                subject = "Password Reset Request"
                message = (
                    "To reset your password click the link below to reset password "
                    f"Reset your password\n{url}"
                )
                try:
                    print(message, subject, settings.EMAIL_HOST_USER)
                    send_mail(
                        subject,
                        message,
                        settings.EMAIL_HOST_USER,
                        [email],
                    )
                    print(
                        f"\n Subject ={subject}\n message = {message}\n Host = {settings.EMAIL_HOST_USER}\n mail = {email}"
                    )
                    return redirect("/")
    
                except Exception as e:
                    print(e,"error")
                    return render(request, "forgot.html")
                    

            else:
                print(f"Invalid email address")
            return render(request, "forgot.html")


class Resetpassword(View):
    def get(self, request, uuid ):
        context = {'uuid':uuid}
        return render(request, "resetpassword.html",context)

    def post(self, request, uuid):
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        
        current_date_time = datetime.datetime.now()
        
        obj = resetuuid.objects.get(UUID = uuid)
        user = obj.user
        current_time = current_date_time.timezone('UTC')
        
        if new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            return redirect('/')
        else:
            print("link expired")
            return redirect('/')
        
class questions(View):
    def get(self, request):
        data = Question.objects.all()
        print(data)
        context = {"data":data}
        return render(request, "question.html",context)
    
    def post(self, request):
        question = request.POST.get("question")
        q_type = request. POST.get("q_type")
        if q_type == "is_mcq":
            pass
        elif q_type== "is_theory":
            pass
        