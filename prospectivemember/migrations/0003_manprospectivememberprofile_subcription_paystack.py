# Generated by Django 3.2.13 on 2023-04-30 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospectivemember', '0002_auto_20230430_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='manprospectivememberprofile',
            name='subcription_paystack',
            field=models.CharField(default='', max_length=300),
        ),
    ]
