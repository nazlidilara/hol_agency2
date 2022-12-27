from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from django.db.models import ForeignKey
from django.urls import reverse
# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smptpserver = models.CharField(blank=True, max_length=30)
    smptemail = models.CharField(blank=True, max_length=30)
    smptpassword = models.CharField(blank=True, max_length=150)
    smptport = models.CharField(blank=True, max_length=15)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    aboutus = models.TextField(max_length=5050)
    contact = models.CharField(max_length=50)
    contact_map = models.CharField(max_length=50)
    references = models.TextField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    uptade_at = models.DateTimeField(auto_now=True)
    price=models.FloatField()
    image=models.ImageField(blank=True,upload_to='images/')

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=15)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/userProfile')


    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'city', 'country', 'image']


class  Products(models.Model):

    category = models.CharField(max_length=200,blank=True)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255,blank=True)
    description = models.CharField(max_length=255,blank=True)
    price= models.FloatField(null=True)
    image = models.ImageField(blank=True,upload_to="images/")
    detail = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True,null=True)
    uptade_at = models.DateTimeField(auto_now=True,null=True)

class Images(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    image=models.ImageField(blank=True,upload_to='images/')

    def __str__(self):
        return self.title


class ContactFormMessage(models.Model):
    STATUS = (
        ('new','new'),
        ('read','read'),
    )
    name = models.CharField(blank=True, max_length=25)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=150)
    message = models.CharField(blank=True, max_length=250)
    ip= models.CharField(blank=True, max_length=50)
    note = models.CharField(blank=True,max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    uptade_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class HomeSlider(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,default="")
    subTitle = models.CharField(max_length=200)
    product_Image = models.ImageField(upload_to="images",null=True)
    see_on_slider = models.BooleanField(default=False)
    description = models.TextField()
    category_of_the_month = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    featured_product = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}",


class ContactForm(models.Model):
    name=models.CharField(max_length=100,null=True)
    eMail=models.CharField(max_length=100,null=True)
    subject=models.CharField(max_length=200,null=True)
    message=models.CharField(max_length=1000,null=True)


