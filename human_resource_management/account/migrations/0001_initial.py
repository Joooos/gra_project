# Generated by Django 2.1 on 2019-03-05 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Informationofstaff',
            fields=[
                ('userid', models.CharField(db_column='userID', max_length=50, primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='userName', max_length=50)),
                ('userpwd', models.CharField(db_column='userPwd', max_length=50)),
                ('department', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('userage', models.IntegerField(db_column='userAge')),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('power_info', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'informationofstaff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('chkid', models.IntegerField(db_column='chkID', primary_key=True, serialize=False)),
                ('userid', models.CharField(db_column='userID', max_length=50)),
                ('chk_late', models.IntegerField()),
                ('chk_leave_early', models.IntegerField()),
                ('chk_vacation', models.CharField(max_length=50)),
                ('chk_casual', models.CharField(max_length=50)),
                ('chk_sick', models.CharField(max_length=50)),
                ('chk_date', models.DateTimeField()),
                ('telephone', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'temp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('account_number', models.IntegerField(default='0')),
                ('real_name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('starting_date', models.DateField()),
                ('date_of_birth', models.DateTimeField()),
                ('age', models.IntegerField(default='0')),
                ('education', models.CharField(max_length=50)),
                ('gender', models.BooleanField()),
                ('is_inservice', models.BooleanField(default='0')),
                ('political_status', models.CharField(max_length=20)),
                ('cellphone', models.IntegerField(default='0')),
                ('office_number', models.IntegerField(default='0')),
                ('office_email', models.EmailField(default='', max_length=254)),
                ('remark', models.TextField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
