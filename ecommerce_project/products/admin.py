from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, ProductImage, ProductVariant


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ['preview']

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" height="60" style="object-fit:cover; border-radius:6px;" />', obj.image.url)
        return "—"
    preview.short_description = "Image Preview"


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1
    fields = ('name', 'price', 'stock')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'name', 'category', 'price', 'discount_price', 'stock', 'is_featured')
    list_filter = ('category', 'is_featured')
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_featured',)
    inlines = [ProductImageInline, ProductVariantInline]

    def thumbnail(self, obj):
        if obj.main_image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover; border-radius:6px;" />', obj.main_image.url)
        return "—"
    thumbnail.short_description = "Image"