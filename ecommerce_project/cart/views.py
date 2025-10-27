# cart/views.py
from django.views.generic import TemplateView, View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from products.models import Product
from .models import CartItem

@method_decorator(login_required, name='dispatch')
class CartView(TemplateView):
    template_name = 'cart/cart_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_items = CartItem.objects.filter(user=self.request.user)
        total = sum(item.subtotal() for item in cart_items)
        context.update({
            'cart_items': cart_items,
            'total': total,
        })
        return context


@method_decorator(login_required, name='dispatch')
class AddToCartView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        cart_item.quantity += 1
        cart_item.save()
        return redirect('cart_detail')


@method_decorator(login_required, name='dispatch')
class RemoveFromCartView(View):
    def post(self, request, pk):
        cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
        cart_item.delete()
        return redirect('cart_detail')


@method_decorator(login_required, name='dispatch')
class UpdateQuantityView(View):
    def post(self, request, pk):
        cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
        action = request.POST.get('action')

        if action == 'increase':
            cart_item.quantity += 1
        elif action == 'decrease' and cart_item.quantity > 1:
            cart_item.quantity -= 1

        cart_item.save()
        return redirect('cart_detail')