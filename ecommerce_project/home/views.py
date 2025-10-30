# views.py
from django.views.generic import TemplateView
from products.models import Category, Product

class HomePageView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()

        # Fetch featured products (make sure your Product model has a BooleanField like 'is_featured')
        context['featured_products'] = Product.objects.filter(is_featured=True)[:8]
        return context