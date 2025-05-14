# account/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, DoctorProfile, PatientProfile


class UserAdminCustom(UserAdmin):
    model = User
    list_display = ['username', 'email', 'is_doctor', 'is_patient', 'is_active']
    list_filter = ['is_doctor', 'is_patient', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['date_joined']

    # enable is_doctor and is_patient in edit form
    fieldsets = UserAdmin.fieldsets + (
        ('User Role', {'fields': ('is_doctor', 'is_patient')}),
    )

    # also show in user creation form (optional)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('User Role', {
            'classes': ('wide',),
            'fields': ('is_doctor', 'is_patient')}
        ),
    )


admin.site.register(User, UserAdminCustom)
admin.site.register(DoctorProfile)
admin.site.register(PatientProfile)
