from django.db import models

# Create your models here.
from django.db import models

class Income_Entry_Form(models.Model):
    income_time = models.DateTimeField()
    income_salary = models.FloatField()
    income_type = models.CharField(max_length=30)
    income_remark = models.TextField()


class Expenditure_Entry_Form(models.Model):
    expenditure_time = models.DateTimeField()
    expenditure_salary = models.FloatField()
    expenditure_type = models.CharField(max_length=30)
    expenditure_remark = models.TextField()