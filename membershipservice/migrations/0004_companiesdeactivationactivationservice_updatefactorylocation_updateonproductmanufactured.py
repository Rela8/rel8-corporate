# Generated by Django 3.2.13 on 2023-06-23 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membershipservice', '0003_auto_20230621_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateOnProductManufactured',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=10)),
                ('most_recent_finicial_statement', models.FileField(blank=True, default=None, null=True, upload_to='most_recent_finicial_statement/%d/')),
                ('product_report_for_branch_inspection', models.FileField(blank=True, default=None, null=True, upload_to='product_report_for_branch_inspection/%d/')),
                ('members_reissuanceform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membershipservice.membersreissuanceform')),
            ],
        ),
        migrations.CreateModel(
            name='UpdateFactoryLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=10)),
                ('most_recent_finicial_statement', models.FileField(blank=True, default=None, null=True, upload_to='most_recent_finicial_statement/%d/')),
                ('product_report_for_branch_inspection', models.FileField(blank=True, default=None, null=True, upload_to='product_report_for_branch_inspection/%d/')),
                ('members_reissuanceform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membershipservice.membersreissuanceform')),
            ],
        ),
        migrations.CreateModel(
            name='CompaniesDeactivationActivationService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=10)),
                ('letter_request_for_activation_or_deactivation', models.FileField(blank=True, default=None, null=True, upload_to='letter_request_for_activation_or_deactivation/%d/')),
                ('submit_original_membership_cert', models.FileField(blank=True, default=None, null=True, upload_to='submit_original_membership_cert/%d/')),
                ('members_reissuanceform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membershipservice.membersreissuanceform')),
            ],
        ),
    ]
