# Generated by Django 4.1.7 on 2023-04-03 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fraud_App', '0009_transaction_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='Fruad',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]