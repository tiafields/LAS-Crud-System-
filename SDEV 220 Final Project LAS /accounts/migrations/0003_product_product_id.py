# Generated by Django 4.2 on 2023-05-07 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_products_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_ID',
            field=models.FloatField(null=True),
        ),
    ]