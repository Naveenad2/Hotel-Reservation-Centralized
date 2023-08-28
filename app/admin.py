from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(Hotels)
admin.site.register(Location)
admin.site.register(Bookings)

