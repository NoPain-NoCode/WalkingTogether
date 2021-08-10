from django.contrib import admin

from .models import User, SocialPlatform, Pet

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'nickname')
    
    def has_delete_permission(self, request, obj=None):
        return True
        
admin.site.register(User, UserAdmin)


class SocialPlatformAdmin(admin.ModelAdmin):
    list_display = ('platform',)
        
admin.site.register(SocialPlatform, SocialPlatformAdmin)


class PetAdmin(admin.ModelAdmin):
    list_display = ('pet_name', 'owner', 'gender')
        
admin.site.register(Pet, PetAdmin)