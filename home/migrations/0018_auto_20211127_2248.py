# Generated by Django 3.2.9 on 2021-11-27 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_edit_collegeid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueid', models.CharField(blank=True, default='Not Provided', max_length=122, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='edit',
            name='collegeid',
            field=models.CharField(blank=True, default='Not Provided', max_length=122, null=True),
        ),
    ]
