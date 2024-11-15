from django.urls import path
from .views import *

urlpatterns = [
    path("", loginview.as_view(), name="login"),
    path("signup/", signup.as_view(), name="signup"),
    path("logout/", logoutview.as_view(), name="logout"),
    path("forgot/", Forgot.as_view(), name= "forgot"),
    path("reset/<uuid:uuid>", Resetpassword.as_view(), name="resetpassword"),
    path("index/", index.as_view(), name="index"),
    
    path('questions/',questions.as_view(),name ="questions")
]
