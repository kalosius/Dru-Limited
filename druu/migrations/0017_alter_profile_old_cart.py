# Generated by Django 5.0.6 on 2024-06-13 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('druu', '0016_alter_profile_old_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='old_cart',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
