from django.core.validators import validate_email
from django.utils import timezone
from django.db import models

import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from django.core.files import File

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, validators=[validate_email])

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    barcode = models.CharField(max_length=50)
    barcode_image = models.ImageField(upload_to='barcodes/', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        COD128 = barcode.get_barcode_class('code128')
        rv = BytesIO()
        code = COD128(f'{self.barcode}', writer=ImageWriter()).write(rv)
        self.barcode_image.save(f'{self.id}.png', File(rv), save=False)
        return super().save(*args, **kwargs)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderProduct')
    created_at = models.DateTimeField(default=timezone.now)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
