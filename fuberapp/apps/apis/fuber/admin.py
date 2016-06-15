from django.contrib import admin
from .models import Cab, CabBooking


class CabAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver_name', 'cab_type', 'number', 'color')
    list_filter = ('is_assigned',)


class CabBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'fare', 'cab')
    list_filter = ('is_running',)

admin.site.register(Cab, CabAdmin)
admin.site.register(CabBooking, CabBookingAdmin)
