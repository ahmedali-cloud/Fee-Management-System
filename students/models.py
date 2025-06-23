# from django.db import models

# class Student(models.Model):
#     GR_number = models.CharField(max_length=20, primary_key=True)
#     name = models.CharField(max_length=100)
#     student_class = models.CharField(max_length=50)
#     guardian_name = models.CharField(max_length=100)
#     contact_number = models.CharField(max_length=15)
#     admission_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name} ({self.student_class})"



# from django.db import models
# from students.models import Student

# class Fee(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     fee_month = models.DateField()
#     amount = models.DecimalField(max_digits=8, decimal_places=2)
#     paid_amount = models.DecimalField(max_digits=8, decimal_places=2)
#     fine = models.DecimalField(max_digits=6, decimal_places=2, default=0)
#     payment_date = models.DateField(auto_now_add=True)
#     payment_mode = models.CharField(max_length=50, choices=[
#         ('Cash', 'Cash')  # Only cash now
#     ])

#     def due_amount(self):
#         return self.amount - self.paid_amount + self.fine

#     def __str__(self):
#         return f"Fee: {self.student.GR_number} - {self.fee_month.strftime('%B %Y')}"
    

from django.db import models

class Student(models.Model):
    GR_number = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)
    guardian_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    admission_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.student_class})"

