# Generated by Django 3.2.9 on 2021-11-26 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20211126_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit',
            name='proof',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='edit',
            name='status',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
    ]
