# Generated by Django 3.2.13 on 2023-07-12 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospectivemember', '0019_manprospectivememberprofile_executive_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='manprospectivememberprofile',
            name='review_text',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='manprospectivememberprofile',
            name='application_status',
            field=models.CharField(choices=[('application_pending', 'Application Pending'), ('acknowledgement_of_application', 'Acknowledgement Of Application'), ('inspection_of_factory_inspection', 'Inspection Of Factory Inspection'), ('ready_for_presentation_of_national_council', 'Ready For Presentation Of National Council'), ('approval_in_progress', 'Approval In Progress'), ('decline', 'Decline'), ('final_approval', 'Final Approval'), ('rework', 'Rework')], default='approval_in_progress', max_length=100),
        ),
    ]
