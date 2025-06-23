from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['GR_number', 'name', 'student_class', 'contact_number', 'admission_date']
    search_fields = ['name', 'GR_number']
    list_filter = ['student_class']


# students/admin.py

# from django.contrib import admin
# from .models import Student

# class StudentAdmin(admin.ModelAdmin):
#     search_fields = ['GR_number']

