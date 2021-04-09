from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Drug)
admin.site.register(Pharmacy)
admin.site.register(Role)
admin.site.register(Coordinate)
admin.site.register(Pharmacy_Drug)
admin.site.register(Favourite_Drug)
admin.site.register(Favourite_Pharmacy)
admin.site.register(Transaction)