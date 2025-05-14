from django.contrib import admin
from .models import TimeSlot, Appointment


class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'date', 'start_time', 'end_time', 'is_reserved']
    list_filter = ['doctor', 'date', 'is_reserved']


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'time_slot', 'created_at']
    list_filter = ['patient', 'time_slot__doctor', 'time_slot__date']


admin.site.register(TimeSlot, TimeSlotAdmin)
admin.site.register(Appointment, AppointmentAdmin)
