# Generated by Django 4.1.7 on 2023-04-04 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fraud_App', '0011_rename_fruad_transaction_fraud'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='Date',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
