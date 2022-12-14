# Generated by Django 4.1 on 2022-11-30 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_cart_created_at_remove_cart_item_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='name',
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(related_name='products', to='api.menu'),
        ),
        migrations.AlterModelTable(
            name='cart',
            table='api_cart',
        ),
    ]
