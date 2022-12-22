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
    list_display = ['title', 'image_tag']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}



class imagesAdmin(admin.ModelAdmin):
    list_display = ['title','product','images']





# Register your models here.
admin.site.register(Category, categoryAdmin)
admin.site.register(Product,productAdmin)
admin.site.register(Images,imagesAdmin)
admin.site.register(Comment)