from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import mark_safe


class Banner(models.Model):
    img=models.ImageField(upload_to="banner_imgs/")
    alt_text=models.CharField(max_length=300)

    class Meta:
        verbose_name_plural='Banners'
        
    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url))

    def __str__(self):
        return self.alt_te
#Category model class
class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    image=models.ImageField(upload_to="cat_imgs/")
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.image.url))

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.title

#Brand Model Class
class Brand(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="brand_imgs/")

    class Meta:
        verbose_name_plural='Brands'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.image.url))

    def __str__(self):
        return self.title



# Color Model Class
class Color(models.Model):
    title=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Colors'
    def color_bg(self):
        return mark_safe('<div style="width:30px; height:25px; background-color:%s"></div>' % (self.color_code))
    def __str__(self):
        return self.title

# Size Model class
class Size(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Sizes'

    def __str__(self):
        return self.title

# Product Model Class
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand =models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    slug = models.SlugField(max_length=255)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    


    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)
    
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])
    


    def __str__(self):
        return self.title

class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    price=models.PositiveIntegerField(default=0)
    image=models.ImageField(upload_to="product_imgs/",null=True)

    class Meta:
        verbose_name_plural='ProductAttributes'

    
    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url))

    def __str__(self):
        return self.product.title