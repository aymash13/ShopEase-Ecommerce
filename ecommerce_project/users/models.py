from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# --------------------------------------------------
# 1️⃣ Profile Model - extends Django's built-in User
# --------------------------------------------------
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', default='default.png', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['user__username']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


# --------------------------------------------------
# 2️⃣ Address Model - supports multiple addresses per user
# --------------------------------------------------
class Address(models.Model):
    ADDRESS_TYPES = (
        ('shipping', 'Shipping'),
        ('billing', 'Billing'),
    )

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='addresses')
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50, default='India')

    address_type = models.CharField(max_length=20, choices=ADDRESS_TYPES, default='shipping')
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.full_name} - {self.city} ({self.address_type})"

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        ordering = ['-created_at']