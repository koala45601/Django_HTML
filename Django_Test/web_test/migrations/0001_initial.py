# Generated by Django 3.2.4 on 2021-07-03 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock_Me',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stock_name', models.CharField(max_length=100)),
                ('Stock_ID', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('Meet', 'Meet'), ('Farm', 'Farm'), ('Tools', 'Tools'), ('Book', 'Book')], default='Meet', max_length=200)),
                ('Stock_remark', models.CharField(max_length=200)),
            ],
        ),
    ]
