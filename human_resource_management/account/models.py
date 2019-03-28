# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Informationofstaff(models.Model):
    userid = models.CharField(db_column='userID', primary_key=True, max_length=50)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=50)  # Field name made lowercase.
    userpwd = models.CharField(db_column='userPwd', max_length=50)  # Field name made lowercase.
    department = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    userage = models.IntegerField(db_column='userAge')  # Field name made lowercase.
    email = models.CharField(max_length=50, blank=True, null=True)
    power_info = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'informationofstaff'


class Temp(models.Model):
    chkid = models.IntegerField(db_column='chkID', primary_key=True)  # Field name made lowercase.
    userid = models.CharField(db_column='userID', max_length=50)  # Field name made lowercase.
    chk_late = models.IntegerField()
    chk_leave_early = models.IntegerField()
    chk_vacation = models.CharField(max_length=50)
    chk_casual = models.CharField(max_length=50)
    chk_sick = models.CharField(max_length=50)
    chk_date = models.DateTimeField()
    telephone = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'temp'

class UserProfile(models.Model):

    # 增加的属性
    picture = models.ImageField(upload_to='profile_images', blank=True)
    account_number = models.IntegerField(default="0")  # 员工账号
    real_name = models.CharField(max_length=50, )
    department = models.CharField(max_length=50, )
    position = models.CharField(max_length=50, )
    starting_date = models.DateField()
    personal_id = models.BigIntegerField(default="0")
    date_of_birth = models.DateTimeField()
    age = models.IntegerField(default="0")
    education = models.CharField(max_length=50)
    gender = models.BooleanField()
    is_inservice = models.BooleanField(default="0")
    political_status = models.CharField(max_length=20)
    user_id = models.CharField(max_length=50)
    # 表格三少
    cellphone = models.BigIntegerField(default="0")
    office_number = models.BigIntegerField(default="0")
    office_email = models.EmailField(default="")
    # 备注大文本
    remark = models.TextField(default="")


class TestModel(models.Model):
    SELVALUE = (
        ('标题', 'first'),  # 前面是展示在前端界面的内容,后面的'first'是真正存在数据库中的
        ('内容', 'second'),
        ('作者', 'third'),
    )
    select_value = models.CharField(max_length=10, choices=SELVALUE)
