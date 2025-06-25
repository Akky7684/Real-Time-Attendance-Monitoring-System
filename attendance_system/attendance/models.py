from django.db import models
from django.contrib.auth.models import User
from datetime import date

# 🔄 Extended User model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    aruco_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.user.username

# ✅ Keep this model for attendance tracking
class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"

