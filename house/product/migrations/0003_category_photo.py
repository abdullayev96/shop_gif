# Generated by Django 3.2.4 on 2023-04-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_customer_delete_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
