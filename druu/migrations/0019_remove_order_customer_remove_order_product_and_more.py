# Generated by Django 5.0.6 on 2024-06-22 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('druu', '0018_rename_phone_number_customer_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
