from django.contrib import admin
# Register your models here.
from .models import Item
admin.site.register(Item)

from .models import Unit
admin.site.register(Unit)

from .models import Customer
admin.site.register(Customer)

from .models import SalesPurchases
admin.site.register(SalesPurchases)
