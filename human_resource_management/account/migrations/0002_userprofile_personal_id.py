# Generated by Django 2.1 on 2019-03-05 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='personal_id',
            field=models.IntegerField(default='0'),
        ),
    ]
