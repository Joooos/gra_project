# Generated by Django 2.1 on 2019-03-17 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payroll_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll_Entry_Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default='0')),
                ('month', models.IntegerField(default='0')),
                ('department', models.CharField(max_length=50)),
                ('real_name', models.CharField(max_length=50)),
                ('basic_salary', models.FloatField()),
                ('phone_allowance', models.FloatField()),
                ('overtime_days', models.IntegerField(default='0')),
                ('overtime_salary', models.FloatField()),
                ('absence_days', models.IntegerField(default='0')),
                ('absence_salary', models.FloatField()),
                ('other_deduction', models.FloatField()),
                ('other_withholding', models.FloatField()),
                ('personal_income_tax', models.FloatField()),
            ],
        ),
    ]