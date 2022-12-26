from django.contrib import admin

from product.models import Category, Product, Images, Comment


# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display = ['title','description']
    list_filter = ['status']
    prepopulated_fields = {'slug': ('title',)}
class ProductImageInline(admin.TabularInline):
    model = Images
    Extra = 5

class productAdmin(admin.ModelAdmin):
    list_display = ['title','category']
    inlines = [ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}




class imagesAdmin(admin.ModelAdmin):
    list_display = ['title','product','image_tag']
    readonly_fields = ('image_tag',)

class commentAdmin(admin.ModelAdmin):
    list_display = ['subject','status']
    list_filter = ['status']




# Register your models here.
admin.site.register(Category, categoryAdmin)
admin.site.register(Product,productAdmin)

admin.site.register(Comment)
