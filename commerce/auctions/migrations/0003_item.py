# Generated by Django 3.0.8 on 2020-07-12 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_user_value_of_items_purchased_before'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_description', models.CharField(max_length=200)),
                ('item_name', models.CharField(max_length=64)),
                ('item_price', models.DecimalField(decimal_places=2, default=999.99, max_digits=5)),
                ('stock_available', models.IntegerField()),
            ],
        ),
    ]
