from django.db import models

# Create your models here.
class Attendance_Record(models.Model):
    # 姓名 打卡时间 打卡类型 加班时长
    name = models.CharField(max_length=128)
    check_in_time = models.DateTimeField()
    check_in_type = models.CharField(max_length=128)
    overtime_hours = models.FloatField()
    leave_days = models.FloatField()
