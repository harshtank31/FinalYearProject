# Generated by Django 4.1.7 on 2023-03-30 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fraud_App', '0006_userdetails_city_userdetails_ip_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='City',
        ),
    ]
