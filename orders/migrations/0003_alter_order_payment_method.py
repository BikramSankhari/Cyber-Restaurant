# Generated by Django 5.0 on 2024-02-01 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Paypal', 'Paypal'), ('Razorpay', 'Razorpay')], max_length=8),
        ),
    ]
