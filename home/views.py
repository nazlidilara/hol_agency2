from django.contrib.auth import authenticate, login, logout
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect

from home.models import Setting, UserProfile,ContactFormMessage,HomeSlider,ContactForm
from product.models import Category, Product, Images, Comment


# Create your views here.

def index_request(request):
    homeSlider=HomeSlider.objects.all()
    settingico = Setting.objects.all()
    setting=Setting.objects.get(pk=1)
    sliderdata=Product.objects.all()[:3]
    category = Category.objects.all()
    dayproducts = Product.objects.all()[:4]
    lastproducts = Product.objects.all().order_by('-id')[0:4]
    randomproducts =Product.objects.all().order_by('?')[0:4]
    context = {'category': category,
               'dayproducts': dayproducts,
               'lastproducts': lastproducts,
               'randomproducts': randomproducts,
               'sliderdata':sliderdata,
               'homeSlider':homeSlider }
    return render(request, 'index.html',context)


def category_products(request, id, slug):
    category = Category.objects.all()
    selectedCategory = Category.objects.filter(pk=id)
    product = Product.objects.filter(category_id=id,slug=slug)
    context = {'selectedCategory': selectedCategory,
               'products': product,
               'category':category,
               'images': images }
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
    setting=Setting.objects.get(pk=1)
    context={'setting':setting}
    return render(request,"about.html")

def blog_request(request):
    return render(request,"blog.html")

def blogdetail_request(request):
    return render(request,"blogdetail.html")



def destination_request(request):
    return render(request,"destination.html")

def service_request(request):
    return render(request,"service.html")

def register_request(request):
    return render(request,"register.html")

def contact(request):
    if request.method == 'POST':
        name=request.POST['name']
        eMail=request.POST['eMail']
        subject=request.POST['subject']
        message=request.POST['message']

        '''from django.core.mail import send_mail

        send_mail(
        f'Bir mesajınız var !',
        f'Web Sayfanız Üzerinden Sizinle iletişime geçmek istiyor:{name}',
        f'Konu:{message},',

        'dilaraaksoy6@hotmail.com',
        ['dilaraaksoy6@hotmail.com','dilaraaksoy6@hotmail.com'],
        fail_silently=False,
         )'''

        s=ContactForm(name=name,eMail=eMail,subject=subject,message=message)
        s.save()

        return redirect('home')

    else:
        return render(request,"contact.html")

