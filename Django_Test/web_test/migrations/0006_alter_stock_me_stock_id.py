# Generated by Django 3.2.4 on 2021-07-13 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_test', '0005_alter_stock_me_socrce'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_me',
            name='Stock_ID',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
