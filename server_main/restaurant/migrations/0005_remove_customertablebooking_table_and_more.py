# Generated by Django 5.0.1 on 2024-01-31 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
        ('restaurant', '0004_customertablebooking_amount_paid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customertablebooking',
            name='table',
        ),
        migrations.AddField(
            model_name='customertablebooking',
            name='tables',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='resturenttables',
            name='booked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authApp.customer'),
        ),
    ]
