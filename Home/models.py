from django.db import models
from django import forms
from PIL import Image
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone

class Product(models.Model):
    class Categories(models.TextChoices):
        FIELD_CROPS = 'FC', 'Field Crops'
        VEGETABLES_SEEDS = 'VS', 'Vegetable Seeds'

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(default = 'default.jpg',upload_to = 'product_pics')
    category = models.CharField(max_length = 2, choices = Categories.choices, default = None)
    slug = models.SlugField(max_length = 250, unique = True)
    seller = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)

           # img = img.convert('RGB')  # Convert image to RGB format
            img.save(self.image.path)  # Save image as JPEG
        
        if not self.slug:
            self.slug = slugify(self.name)
        while Product.objects.filter(slug=self.slug).exists():
            self.slug = f'{slugify(self.name)}-{timezone.now().strftime("%Y%m%d%H%M%S")}'
        super(Product, self).save(*args, **kwargs)


class Order(models.Model):
    # Fields for the order
    seller = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders_sold')
    buyer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='orders_purchased')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product')
    quantity = models.PositiveIntegerField()
    net_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ], default='PENDING')

    # Other fields (if needed)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id}"