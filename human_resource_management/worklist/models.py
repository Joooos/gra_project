from django.db import models

# Create your models here.
class worklists(models.Model):
    # 提出人 负责人 提出时间 工作名称 内容 计划完成时间
    proposer = models.CharField(max_length=128)
    person_in_charge = models.CharField(max_length=200)
    proposed_time = models.DateTimeField()
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    planned_completion_time = models.DateTimeField()