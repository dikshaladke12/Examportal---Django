from django.urls import path
from .views import *

urlpatterns = [
    path("", loginview.as_view(), name="login"),
    path("signup/", signup.as_view(), name="signup"),
    path("logout/", logoutview.as_view(), name="logout"),
    path("index/", index.as_view(), name="index"),
]
