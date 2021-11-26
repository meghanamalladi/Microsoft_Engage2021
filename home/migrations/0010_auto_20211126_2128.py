# Generated by Django 3.2.9 on 2021-11-26 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_edit_verification_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit',
            name='College_ID',
            field=models.CharField(blank=True, default='Not Provided', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='edit',
            name='proof',
            field=models.CharField(blank=True, choices=[('Aadhar', 'Aadhaar Card'), ('PAN', 'PAN Card')], default='Not Provided', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='edit',
            name='status',
            field=models.CharField(blank=True, choices=[('Red', 'Not yet Vaccinated'), ('Yellow', 'Partially Vaccinated'), ('Green', 'Fully Vaccinated')], default='Not Provided', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='edit',
            name='verification_ID',
            field=models.CharField(blank=True, default='Not Provided', max_length=50, null=True),
        ),
    ]