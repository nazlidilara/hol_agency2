from django.contrib.auth import authenticate, login, logout
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.models import Setting, UserProfile
from product.models import Category, Product, Images, Comment


# Create your views here.

def index_request(request):
    '''category = Category.objects.all()
    dayproducts = Product.objects.all()[:4]
    lastproducts = Product.objects.all().order_by('-id')[0:4]
    randomproducts =Product.objects.all().order_by('?')[0:4]
    context = {'category': category,
               'dayproducts': dayproducts,
               'lastproducts': lastproducts,
               'randomproducts': randomproducts}'''
    return render(request, 'index.html')


def category_products(request, id, slug):
    category = Category.objects.all()
    selectedCategory = Category.objects.filter(pk=id)
    product = Product.objects.filter(category_id=id,slug=slug)
    context = {'selectedCategory': selectedCategory,
               'products': product,
               'category':category}
    return render(request, 'category_products.html', context)


def product_detail(request, id, slug):
    category = Category.objects.all()
    selectedProduct = Product.objects.filter(pk=id)
    productImages = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status='True')
    context = {'category': category,
               'selectedProduct': selectedProduct,
               'productImages': productImages,
               'comments': comments}
    return render(request, 'product_detail.html', context)



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    context = {'category': category, }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')



def about_request(request):

    #bu kısıma istediğin foknsiyonu veya db yi koyarsın......
    return render(request,"about.html")
