# Generated by Django 5.0.3 on 2024-03-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
