# Generated by Django 3.0.5 on 2020-06-11 04:14

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bss_set1',
            name='intangible_asset',
            field=models.DecimalField(decimal_places=3, default=Decimal('0.0000'), max_digits=15),
        ),
    ]
