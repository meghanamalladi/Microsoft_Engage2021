# Generated by Django 3.2.9 on 2021-11-26 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_verification_id_edit_verificationid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit',
            name='proof',
            field=models.CharField(blank=True, default='Not Provided', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='edit',
            name='status',
            field=models.CharField(blank=True, default='Not Provided', max_length=122, null=True),
        ),
    ]
