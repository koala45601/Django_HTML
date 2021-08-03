# Generated by Django 3.2.4 on 2021-07-10 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_test', '0002_stock_me_socrce'),
    ]

    operations = [
        migrations.CreateModel(
            name='Local_stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provi', models.CharField(choices=[('Bangkok', 'Bangkok'), ('ChiangMai', 'ChiangMai'), ('ChiangRai', 'ChiangRai'), ('Kamphaeng', 'Kamphaeng')], default='Bangkok', max_length=100)),
                ('Stock_name', models.CharField(max_length=200)),
                ('Stock_ID', models.CharField(max_length=4)),
                ('manager_name', models.CharField(max_length=100)),
                ('branch_Tel', models.CharField(max_length=10)),
                ('Stock_remark', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
