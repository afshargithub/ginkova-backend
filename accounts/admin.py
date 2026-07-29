# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .models import UserAddress


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            'Additional Information',
            {
                'fields': (
                    'phone',
                    'language',
                )
            }
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'username',
                    'email',
                    'phone',
                    'language',
                    'password1',
                    'password2',
                ),
            },
        ),
    )

    list_display = (
        'id',
        'username',
        'email',
        'phone',
        'language',
        'is_staff',
        'is_active',
    )
    
    
    
@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'title',
        'city',
        'address_type',
        'is_default',
        'is_active',
        'created_at',
    )


    list_filter = (
        'is_active',
        'is_default',
        'address_type',
        'city',
    )


    search_fields = (
        'user__username',
        'user__email',
        'address_line',
        'city',
    )