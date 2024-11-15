from django.urls import path
from .views import *

urlpatterns = [
    path("", loginview.as_view(), name="login"),
    path("signup/", signup.as_view(), name="signup"),
    path("logout/", logoutview.as_view(), name="logout"),
    path("forgot/", Forgot.as_view(), name= "forgot"),
    path("resetpassword/", Resetpassword.as_view(), name="resetpassword"),
    path("index/", index.as_view(), name="index"),
]
