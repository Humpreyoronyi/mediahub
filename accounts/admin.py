'''
Import admin avails all inbuid operations for content management
'''
from django.contrib import admin
'''
import the existing config for an admin user 
'''
from django.contrib.auth.admin import UserAdmin
'''
Import the custom user schema/ customs users table
'''
from .models import User

# Register your models here.
# Step : utilize the admin decorator to register your model

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Override the list display to the user info
    list_display = ('username', 'email', 'is_staff', 'user_type', 'is_staff', 'date_joined')

    # Override the filtering of above list
    list_filter = ('user_type', 'is_staff', 'is_superuser')

    # Override what credentials the admin can create 
    # add our custom fields
    # useradmin.fieldsets points to existing django fields then we add our custom fields to it
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', 
        {'fields': ('user_type','profile_image', 'bio')
        }),
    )
    # We add the above fields to django inbuilt admin system
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', 
        {'fields': ('user_type',)
        }),
    )
