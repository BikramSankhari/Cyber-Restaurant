# Generated by Django 5.0 on 2024-02-06 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_details',
        ),
    ]
