# Generated by Django 5.0 on 2024-02-09 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_remove_order_transaction_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_method',
        ),
    ]