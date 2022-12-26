"""hol_agency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from home.views import index_request
from django.contrib import admin
from django.urls import include, path
from home import views
from django.conf.urls.static import static
from account import urlsaccount
urlpatterns = [
    path('',include('home.urls')),
    path('home/',include('home.urls')),
    path('product/',include('product.urls')),
    path('admin/',admin.site.urls),
    path('category/<int:id>/<slug:slug>',views.category_products,name='category_products'),
    path('product/<int:id>/<slug:slug>',views.product_detail,name='product_detail'),
    #path('product/addcomment/<int:id>', views.addcomment, name='addcomment')
    path('account',include(urlsaccount),name='login_view'),

    ]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)