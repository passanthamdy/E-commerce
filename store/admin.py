from django.contrib import admin
from .models import Product , Category,Color, Brand, Size, ProductAttribute,Banner

admin.site.register(Brand)
admin.site.register(Size)

class CategoryAdmin(admin.ModelAdmin):
	list_display=('title','image_tag')
admin.site.register(Category,CategoryAdmin)

class ColorAdmin(admin.ModelAdmin):
	list_display=('title','color_bg')
admin.site.register(Color,ColorAdmin)


class BannerAdmin(admin.ModelAdmin):
	list_display=('alt_text','image_tag')
admin.site.register(Banner,BannerAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','is_active','description',
                    'in_stock', 'created']
    list_filter = ['in_stock', 'is_active']
    list_editable = [ 'in_stock','is_active']
    prepopulated_fields = {'slug': ('title',)}

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display=('product','price','color','size')
admin.site.register(ProductAttribute,ProductAttributeAdmin)
