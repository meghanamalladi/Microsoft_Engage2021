# Generated by Django 3.2.9 on 2021-11-27 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20211127_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(blank=True, default='Not Provided', max_length=122, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Display',
        ),
    ]
