# Generated by Django 3.2.9 on 2021-11-27 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_edit_collegeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edit',
            name='collegeid',
            field=models.CharField(blank=True, default='Not Provided', max_length=122, null=True, unique='True'),
        ),
    ]
