# Generated by Django 5.0 on 2024-01-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('druu', '0004_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default=True, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='partner',
            name='partner_blog',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='social_url',
            field=models.URLField(blank=True, max_length=2856, null=True),
        ),
    ]
