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
    path('guide/',views.guide_request,name='guide'),
    path('sss/',views.sss_request,name='sss'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
)