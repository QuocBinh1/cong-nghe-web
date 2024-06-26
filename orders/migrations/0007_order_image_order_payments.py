# Generated by Django 5.0.1 on 2024-05-28 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_order_payments'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='payments',
            field=models.CharField(choices=[('cod', 'COD'), ('bank transfer', 'Bank Transfer')], default='COD', max_length=50),
        ),
    ]
