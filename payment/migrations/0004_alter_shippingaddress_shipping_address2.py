# Generated by Django 5.0.2 on 2024-03-29 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_rename_shipping_address1_shippingaddress_shipping_address1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='shipping_address2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
