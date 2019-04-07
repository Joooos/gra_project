# Generated by Django 2.1 on 2019-03-29 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='worklists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposer', models.CharField(max_length=128)),
                ('person_in_charge', models.CharField(max_length=200)),
                ('proposed_time', models.DateTimeField()),
                ('project_name', models.CharField(max_length=200)),
                ('project_description', models.TextField()),
                ('planned_completion_time', models.DateTimeField()),
            ],
        ),
    ]
