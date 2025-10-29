from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Order

@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    model = Order
    template_name = 'orders/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')


@method_decorator(login_required, name='dispatch')
class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class CancelOrderView(View):
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk, user=request.user)
        if order.can_cancel:
            order.status = 'CANCELLED'
            order.save()
        return redirect('order_list')