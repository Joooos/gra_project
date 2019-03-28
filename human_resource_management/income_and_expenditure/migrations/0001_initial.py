# Generated by Django 2.1 on 2019-03-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenditure_Entry_Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expenditure_time', models.DateTimeField()),
                ('expenditure_salary', models.FloatField()),
                ('expenditure_type', models.CharField(max_length=30)),
                ('expenditure_remark', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Income_Entry_Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_time', models.DateTimeField()),
                ('income_salary', models.FloatField()),
                ('income_type', models.CharField(max_length=30)),
                ('income_remark', models.TextField()),
            ],
        ),
    ]