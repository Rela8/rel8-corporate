# Generated by Django 3.2.13 on 2023-08-23 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FundAProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('about', models.TextField(default='')),
                ('amount_made', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('image', models.ImageField(default=None, null=True, upload_to='')),
                ('what_project_needs', models.JSONField(default=dict, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryV2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('date_taken', models.DateField()),
                ('chapters', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.chapters')),
            ],
        ),
        migrations.CreateModel(
            name='Ticketing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=300)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SupportProjectInKind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('about', models.TextField(default='')),
                ('member', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.memeber')),
                ('project', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='extras.fundaproject')),
            ],
        ),
        migrations.CreateModel(
            name='SupportProjectInCash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('paystack_key', models.TextField(default='')),
                ('is_paid', models.BooleanField(default=False)),
                ('member', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.memeber')),
                ('project', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='extras.fundaproject')),
            ],
        ),
        migrations.CreateModel(
            name='ImagesForGalleryV2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery_v2/')),
                ('caption', models.TextField(default=' ')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='extras.galleryv2')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField()),
                ('photo_file', models.ImageField(upload_to='gallery/')),
                ('name', models.CharField(max_length=300)),
                ('chapters', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.chapters')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('body', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('fixing', 'Fixing'), ('attended_to', 'Attended To')], default='pending', max_length=50)),
                ('member', models.ForeignKey(blank=True, default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.memeber')),
            ],
        ),
    ]
