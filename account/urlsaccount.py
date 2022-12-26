from django.urls import path
from . import views

urlpatterns = [
    path("login_request",views.login_request,name="login_request"),
    path("logout",views.logout_request,name="logout"),
    path("register",views.register_request,name="register"),

]