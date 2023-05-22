# Generated by Django 3.2.13 on 2023-05-22 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prospectivemember', '0010_manprospectivememberformone_capacity_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manprospectivememberformone',
            name='are_your_product_exported',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='manprospectivememberformone',
            name='company_contact_infomation',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='manprospectivememberformone',
            name='current_sales_turnover',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='manprospectivememberformone',
            name='foreign_share_capital',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='manprospectivememberformone',
            name='installed_capacity',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='manprospectivememberformone',
            name='local_share_capital',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='manprospectivememberformone',
            name='ownership_structure_equity_foregin',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='manprospectivememberformone',
            name='ownership_structure_equity_local',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='manprospectivememberformone',
            name='projected_sales_turnover',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='manprospectivememberformone',
            name='total_value_of_building_asset',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='manprospectivememberformone',
            name='total_value_of_land_asset',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='manprospectivememberformone',
            name='total_value_of_other_asset',
            field=models.TextField(default=' '),
        ),
    ]
