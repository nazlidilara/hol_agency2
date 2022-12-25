from django.contrib import admin

from product.models import Category, Product, Images, Comment


class categoryAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5

class productAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'category','price']

    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}






# Register your models here.
admin.site.register(Category, categoryAdmin)
admin.site.register(Product,productAdmin)

admin.site.register(Comment)
