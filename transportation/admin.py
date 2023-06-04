from django.contrib import admin
from django.db.models import Sum

from .models import *


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ('model', 'number_and_region', 'max_load_capacity', 'max_loading_volume', 'status', 'place',)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    class StockProductInline(admin.StackedInline):
        model = Stock.products.through
        extra = 5

    list_display = ('city', 'address', 'free_volume',)
    inlines = (StockProductInline,)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'price', 'quantity')

    def quantity(self, obj):
        return obj.stockproduct_set.aggregate(quantity=Sum('quantity'))['quantity']


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('source', 'destination', 'status', 'revenue',)
