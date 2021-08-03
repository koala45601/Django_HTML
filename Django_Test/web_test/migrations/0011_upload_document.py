# Generated by Django 3.2.5 on 2021-07-24 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_test', '0010_img_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload_document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userlevel', models.CharField(choices=[('Admin', 'Admin'), ('customer', 'customer')], default='Admin', max_length=50)),
                ('document_name', models.CharField(max_length=150)),
                ('document_up', models.FileField(blank=True, null=True, upload_to='alldoc')),
                ('start_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
