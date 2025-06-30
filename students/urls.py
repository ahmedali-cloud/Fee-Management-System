from django.urls import path
from .views import home_view

urlpatterns = [
    path('home/', home_view, name='home'),  # 👈 name='home' is VERY important!
]
