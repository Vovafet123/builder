from django.contrib import admin

from .models import *


admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Flight)


class TransportAdmin(admin.ModelAdmin):
    search_fields = ('model', 'number_and_region', 'max_load_capacity', 'max_loading_volume', 'status', 'place',)
    list_display = ('model', 'number_and_region', 'max_load_capacity', 'max_loading_volume', 'status', 'place',)


admin.site.register(Transport, TransportAdmin)
