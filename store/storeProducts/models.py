from django.db import models

from Users.models import User
from django.db.models.query import QuerySet
# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name= "Category"
        verbose_name_plural = "categories"
    

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()   
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to='products', null=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name= "Product"
        verbose_name_plural = "products"
    
    def __str__(self):
        return f'Model {self.name} - Category {self.category.name}'
   
class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum for basket in self)
    
    def total_quantity(self):
        return sum(basket.quantity for basket in self)
   
    
class Basket(models.Model):
    user = models.ForeignKey(to = User, on_delete = models.CASCADE )
    product = models.ForeignKey(to= Product, on_delete=models.CASCADE )
    quantity = models.PositiveSmallIntegerField(default=0) 
    created_timestamp = models.DateTimeField(auto_now_add=True)
    
    objects = BasketQuerySet.as_manager()
    
    def __str__ (self):
        return f'Корзина для {self.user.username} | Продукт: {self.product.name}'
    
    @property  
    def sum(self):
        if self.product and self.quantity is not None:
            return self.product.price * self.quantity
        return 0
    

    
 