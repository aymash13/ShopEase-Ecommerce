from django.db import models
from django.conf import settings

class Checkout(models.Model):
    PAYMENT_CHOICES = [
        ('COD', 'Cash on Delivery'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='COD')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Checkout by {self.full_name} ({self.user.username})"