# Generated by Django 5.0.1 on 2024-01-31 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_remove_customertablebooking_table_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerpurchase',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='customerpurchase',
            name='resturent',
        ),
        migrations.DeleteModel(
            name='CustomerOrderItem',
        ),
        migrations.DeleteModel(
            name='CustomerPurchase',
        ),
    ]
