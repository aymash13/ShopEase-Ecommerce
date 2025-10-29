from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price', 'subtotal')

    def subtotal(self, obj):
        return obj.subtotal()
    subtotal.short_description = "Subtotal"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('id', 'user__username')
    ordering = ('-created_at',)
    inlines = [OrderItemInline]

    # Admin can edit status directly from the list view
    list_editable = ('status',)

    readonly_fields = ('user', 'total_amount', 'created_at')

    fieldsets = (
        ('Order Information', {
            'fields': ('user', 'status', 'total_amount', 'created_at')
        }),
    )

    # 🧾 Admin actions to change status quickly
    actions = ['mark_processing', 'mark_shipped', 'mark_delivered', 'mark_cancelled']

    def mark_processing(self, request, queryset):
        updated = queryset.update(status='PROCESSING')
        self.message_user(request, f"{updated} order(s) marked as Processing.")
    mark_processing.short_description = "Mark selected orders as Processing"

    def mark_shipped(self, request, queryset):
        updated = queryset.update(status='SHIPPED')
        self.message_user(request, f"{updated} order(s) marked as Shipped.")
    mark_shipped.short_description = "Mark selected orders as Shipped"

    def mark_delivered(self, request, queryset):
        updated = queryset.update(status='DELIVERED')
        self.message_user(request, f"{updated} order(s) marked as Delivered.")
    mark_delivered.short_description = "Mark selected orders as Delivered"

    def mark_cancelled(self, request, queryset):
        updated = queryset.update(status='CANCELLED')
        self.message_user(request, f"{updated} order(s) marked as Cancelled.")
    mark_cancelled.short_description = "Mark selected orders as Cancelled"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'subtotal_display')

    def subtotal_display(self, obj):
        return obj.subtotal()
    subtotal_display.short_description = "Subtotal"