from django.contrib import admin
from .models import ContactMessage, LensCoating, LensIndex, LensMaterial, PowerRange, LensFeatures, StockLens

class LensMaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Ensure it's a tuple

class LensCoatingAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Ensure it's a tuple

class LensIndexAdmin(admin.ModelAdmin):
    list_display = ('index',)  # Ensure it's a tuple

class LensFeaturesAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Ensure it's a tuple

class StockLensAdmin(admin.ModelAdmin):
    list_display = ('type', 'brand_name', 'lens_index', 'lens_material', 'lens_coating')

class PowerRangeAdmin(admin.ModelAdmin):
    list_display = ('lens_id', 'DIA', 'power_range', 'price_srp')

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

# Register models with their respective custom ModelAdmin classes
admin.site.register(LensMaterial, LensMaterialAdmin)
admin.site.register(LensCoating, LensCoatingAdmin)
admin.site.register(LensIndex, LensIndexAdmin)
admin.site.register(LensFeatures, LensFeaturesAdmin)
admin.site.register(StockLens, StockLensAdmin)
admin.site.register(PowerRange, PowerRangeAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)