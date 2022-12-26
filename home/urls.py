from django.urls import path

from . import views

urlpatterns = (
    path('',views.index_request,name="index"),
    path('home',views.index_request,name="home"),
    path('about',views.about_request,name="about"),
    path('blog',views.blog_request,name="blog"),
    path('blogdetail',views.blog_request,name="blogdetail"),
    path('contact/',views.contact,name='contact'),
    path('destination/',views.destination_request,name='destination'),
    path('service/',views.service_request,name='service'),

)