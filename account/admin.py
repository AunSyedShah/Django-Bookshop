from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile
# Register your models here.
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields':('email','first_name','last_name','password','last_login')}),
        ('Permissions',{'fields':(
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions"
        )}),
    )
    add_fieldsets = (
        (None,
            {
                'classes':('wide',),
                'fields': ('email','password1','password2')
            }
        ),
    )
    list_display = ('email','first_name','last_login')
    list_filter = ('is_active','is_superuser', 'is_staff','groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups',"user_permissions",)

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
