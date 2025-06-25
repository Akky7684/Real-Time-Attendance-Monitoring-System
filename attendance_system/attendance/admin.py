from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import UserProfile, Attendance

# ✅ Show aruco_id in admin panel
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'aruco_id')

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Attendance)
