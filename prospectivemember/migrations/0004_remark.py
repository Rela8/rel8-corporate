# Generated by Django 3.2.13 on 2023-05-16 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prospectivemember', '0003_manprospectivememberprofile_subcription_paystack'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default=' ')),
                ('member_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prospectivemember.manprospectivememberprofile')),
            ],
        ),
    ]
