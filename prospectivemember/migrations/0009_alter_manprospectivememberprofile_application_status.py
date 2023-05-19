# Generated by Django 3.2.13 on 2023-05-17 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospectivemember', '0008_manprospectivememberprofile_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manprospectivememberprofile',
            name='application_status',
            field=models.CharField(choices=[('approval_in_progress', 'Approval In Progress'), ('approval_in_principle_granted', 'Approval In Principle Granted'), ('final_approval', 'Final Approval'), ('decline', 'Decline')], default='approval_in_progress', max_length=100),
        ),
    ]