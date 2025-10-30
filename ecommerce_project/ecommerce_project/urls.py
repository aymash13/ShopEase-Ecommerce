from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# your_project_name/admin.py
from django.contrib import admin

admin.site.site_header = "ShopEase Admin"
admin.site.site_title = "E-Commerce Dashboard"
admin.site.index_title = "Welcome to Admin Panel"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),       # Homepage app
    path('users/', include('users.urls')), # Users app
    path('products/', include('products.urls')), #products
    path('cart/', include('cart.urls')), # cart
    path('orders/', include('orders.urls')), # orders 
    path('checkout/', include('checkout.urls')), #checkout
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)