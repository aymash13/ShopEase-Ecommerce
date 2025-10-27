# cart/models.py
from django.db import models
from django.conf import settings
from products.models import Product

class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        price = self.product.discount_price if self.product.is_on_sale else self.product.price
        return price * self.quantity

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"