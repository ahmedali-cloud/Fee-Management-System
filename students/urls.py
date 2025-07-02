from django.urls import path
from .views import home_view

urlpatterns = [
    path('home/', views.student_home, name='student_home'),
]
