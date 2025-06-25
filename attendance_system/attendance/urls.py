from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('scan/', views.scan_with_intrinsics, name='scan'),
    path('dashboard/', views.dashboard, name='dashboard')

    # dashboard path will be added later
]
