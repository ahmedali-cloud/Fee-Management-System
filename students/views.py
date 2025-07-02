# students/views.py

from django.shortcuts import render

def student_home(request):
    return render(request, 'students/home.html')  # Make sure this is correct
