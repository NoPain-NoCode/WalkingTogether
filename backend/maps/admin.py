from django.contrib import admin
from .models import WalkingTrails, Review, ReviewWalkAvg

class WalkingTrailsAdmin(admin.ModelAdmin):
    list_display = ('point_number', 'point_name', 'category', 'region')

admin.site.register(WalkingTrails, WalkingTrailsAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'walkingtrails', 'user', 'content', 'created_date')

admin.site.register(Review, ReviewAdmin)


class ReviewWalkAvgAdmin(admin.ModelAdmin):
    list_display = ('id', 'walkingtrails', 'point', 'dog_possible')

admin.site.register(ReviewWalkAvg, ReviewWalkAvgAdmin)
