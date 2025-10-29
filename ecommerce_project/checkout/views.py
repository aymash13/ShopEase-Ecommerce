from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .forms import CheckoutForm
from cart.models import CartItem
from orders.models import Order, OrderItem

@method_decorator(login_required, name='dispatch')
class CheckoutView(View):
    def get(self, request):
        form = CheckoutForm()
        cart_items = CartItem.objects.filter(user=request.user)
        total = sum(item.subtotal() for item in cart_items)
        return render(request, 'checkout/checkout.html', {
            'form': form,
            'cart_items': cart_items,
            'total': total,
        })

    def post(self, request):
        form = CheckoutForm(request.POST)
        cart_items = CartItem.objects.filter(user=request.user)
        total = sum(item.subtotal() for item in cart_items)

        if form.is_valid() and cart_items.exists():
            checkout_info = form.save(commit=False)
            checkout_info.user = request.user
            checkout_info.save()

            # Create Order
            order = Order.objects.create(
                user=request.user,
                total_amount=total,
            )

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.discount_price if item.product.is_on_sale else item.product.price
                )

            cart_items.delete()
            return redirect('order_list')  # redirect to order list page

        return render(request, 'checkout/checkout.html', {
            'form': form,
            'cart_items': cart_items,
            'total': total,
        })