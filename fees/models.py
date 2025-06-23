from django.db import models
from students.models import Student

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    FEE_MONTH_CHOICES = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]
    fee_month = models.CharField(max_length=20, choices=FEE_MONTH_CHOICES)

    amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)
    fine = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    payment_date = models.DateField(auto_now_add=True)
    payment_mode = models.CharField(max_length=10, default='Cash')


    def due_amount(self):
        return self.amount - self.paid_amount + self.fine

    def __str__(self):
        return f"Fee: {self.student.name} - {self.fee_month}"
