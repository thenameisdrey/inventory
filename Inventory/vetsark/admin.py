from django.contrib import admin
from .models import NewStock, StockDetails, CustomersDetails, VendorDetails, Purchase, Sales

# Register your models here.

admin.site.register(NewStock),
admin.site.register(StockDetails),
admin.site.register(CustomersDetails),
admin.site.register(VendorDetails),
admin.site.register(Purchase),
admin.site.register(Sales)
