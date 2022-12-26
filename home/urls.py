from django.urls import path

from . import views

urlpatterns = (
    path('',views.index_request,name="index"),
    path('home',views.index_request,name="home"),
    path('about',views.about_request,name="about"),
    path('blog',views.blog_request,name="blog")
)