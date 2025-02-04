from django.contrib import admin
from .models import Supplier, Item


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'email')
    search_fields = ('name', 'email')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'unit_price', 'quantity_in_stock', 'supplier')
    search_fields = ('name', 'sku')
    list_filter = ('category', 'supplier')
