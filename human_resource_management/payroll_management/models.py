from django.db import models

# Create your models here.

class Payroll_Entry_Form(models.Model):
    year = models.IntegerField(default="0")
    month = models.IntegerField(default="0")
    department = models.CharField(max_length=50)
    real_name = models.CharField(max_length=50)
    basic_salary = models.FloatField()
    phone_allowance = models.FloatField()
    overtime_days = models.IntegerField(default="0")
    overtime_salary = models.FloatField()
    absence_days = models.IntegerField(default="0")
    absence_salary = models.FloatField()
    other_deduction = models.FloatField()
    other_withholding = models.FloatField()
    personal_income_tax = models.FloatField()
