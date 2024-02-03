from django.db import models

class ProductManager(models.Manager):
    def get_by_id(self, id):
        try:
            return self.get(id = id)
        except Product.DoesNotExist:
            return None

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    image = models.ImageField(upload_to='products/', null = True, blank = False) 
    
    objects = ProductManager()
       
    def __str__(self):
        return self.title

    objects = ProductManager()   
