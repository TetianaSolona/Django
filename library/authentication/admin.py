from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser 

class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'email', 'created_at', 'updated_at', 'role', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = ()

admin.site.register(CustomUser, AccountAdmin)