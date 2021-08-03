from django.contrib import admin

from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'nickname')
    
    def has_delete_permission(self, request, obj=None):
        return True
        
admin.site.register(User, UserAdmin)