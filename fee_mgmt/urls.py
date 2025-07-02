from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda req: redirect('login')),      
    path('users/', include('users.urls')),         
    path('fees/', include('fees.urls')),
    path('students/', include('students.urls')),   # ✅ ye line zaroori hai
]

