# Generated by Django 2.1 on 2019-03-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20190306_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_id',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
