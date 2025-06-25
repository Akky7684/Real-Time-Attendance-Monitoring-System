from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from .models import Attendance
from datetime import date
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
import cv2
import numpy as np

# 🔹 Mark attendance via POST request (used by detector.py)
def mark_attendance(request):
    if request.method == 'POST':
        aruco_id = int(request.POST.get('aruco_id'))
        try:
            user = User.objects.get(userprofile__aruco_id=aruco_id)
            if not Attendance.objects.filter(user=user, date=date.today()).exists():
                Attendance.objects.create(user=user)
                return JsonResponse({'status': 'marked'})
            else:
                return JsonResponse({'status': 'already_marked'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'user_not_found'})
    return HttpResponse("This endpoint is for POST requests only.")

# 🔹 Register a new user
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'attendance/register.html', {'form': form})

# 🔹 User login
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'attendance/login.html')

# 🔹 User logout
def logout_view(request):
    logout(request)
    return redirect('login')

# 🔹 Dashboard listing all users
@login_required
def dashboard(request):
    return render(request, 'attendance/index.html', {
        "students": User.objects.all()
    })

# 🔹 ARUCO Marker Scanner using OpenCV ≥ 4.7 API
@login_required
def scan_with_intrinsics(request):
    # Camera calibration values (intrinsics)
    camera_matrix = np.array([[976.97, 0., 524.00],
                              [0., 974.93, 362.12],
                              [0., 0., 1.]])
    distortion_coeffs = np.array([[-0.2659, 3.049, -0.0013, -0.0006, -11.933]])

    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
    parameters = cv2.aruco.DetectorParameters()  # ✅ OpenCV ≥ 4.7
    parameters.cornerRef


