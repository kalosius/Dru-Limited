# Generated by Django 5.0 on 2024-01-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('druu', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='uploads/products/'),
        ),
    ]
